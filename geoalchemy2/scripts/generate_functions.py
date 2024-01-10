import re
from collections import OrderedDict
from pathlib import Path
from string import Template
from typing import Any
from typing import Tuple

import black
import psycopg2

from geoalchemy2.types import Geography
from geoalchemy2.types import Geometry
from geoalchemy2.types import GeomVal
from geoalchemy2.types import Raster
from geoalchemy2.types import SummaryStats


def get_function_rows() -> list:
    # Database connection parameters
    db_params = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "",
        "host": "",
        "port": "5432",
    }

    functions_rows = []
    # Connect to the PostgreSQL database
    with psycopg2.connect(**db_params) as conn:
        # Create a cursor object
        with conn.cursor() as cursor:
            # Query to select all functions starting with 'st_' along with their argument types
            # and descriptions
            query = """
            SELECT
                p.proname AS function_name,
                pg_catalog.pg_get_function_result(p.oid) AS return_type,
                pg_catalog.pg_get_function_identity_arguments(p.oid) AS argument_types,
                d.description
            FROM
                pg_catalog.pg_proc p
                LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace
                LEFT JOIN pg_catalog.pg_description d ON p.oid = d.objoid
            WHERE
                p.proname LIKE 'st_%'
                AND n.nspname = 'public'  -- Assuming the functions are in the public schema
            """

            # Execute the query
            cursor.execute(query)

            # Fetch all the rows
            functions_rows = cursor.fetchall()

    return functions_rows


def parse_arg_types(args_str: str) -> Tuple:
    types = {
        "anyelement": Any,
        "bigint": int,
        "boolean": bool,
        "box2d": Geometry,
        "box3d": Geometry,
        "bytea": bytes,
        "cstring": str,
        "double precision": float,
        "geography": Geography,
        "geometry": Geometry,
        "geomval": GeomVal,
        "integer": int,
        "json": str,
        "jsonb": bytes,
        "raster": Raster,
        "record": Any,  # potentially use record-type here?
        "spheroid": str,
        "text": str,
    }
    arg_descs = args_str.replace("OUT ", "").split(", ")
    arg_types = []
    for arg_desc in arg_descs:
        if " " in arg_desc and arg_desc != "double precision":
            arg_desc = arg_desc[arg_desc.index(" ") + 1 :]

        list_ = False
        if arg_desc.endswith("[]"):
            list_ = True
            arg_desc = arg_desc[: len(arg_desc) - 2]

        type_ = types.get(arg_desc, Any).__name__
        type_ = type_ if not list_ else f"List[{type_}]"

        arg_types.append(type_)
    return tuple(arg_types)


all_return_types = set()


def parse_return_type(return_type: str):
    return_types = {
        "anyelement": Any,
        "bigint": int,
        "boolean": bool,
        "box2d": Geometry,
        "box3d": Geometry,
        "bytea": bytes,
        "double precision": float,
        "geography": Geography,
        "geometry": Geometry,
        "geomval": GeomVal,
        "integer": int,
        "raster": Raster,
        "record": Any,  # potentially use record-type here?
        "smallint": int,
        "summarystats": SummaryStats,
        "text": str,
        "void": None,
    }
    list_ = False
    if return_type.endswith("[]"):
        list_ = True
        return_type = return_type[: len(return_type) - 2]
    elif return_type.startswith("SETOF "):
        list_ = True
        return_type = return_type.replace("SETOF ", "")

    type_ = return_types.get(return_type, Any)
    if type_ is not None:
        type_ = type_.__name__

    inst = type_
    if list_:
        type_ = f"List[{type_}]"

    if inst == "Any":
        inst = "object"

    return type_, inst


original_cases = {}


def find_original_case(haystack, needle):
    """Search for a substring in a string return the substring in its original case.

    :param haystack: The string in which to search
    :param needle: The substring to search for
    :return: The substring in its original case if found, else None
    """
    # Use a regular expression to search case-insensitively
    match = re.search(re.escape(needle), haystack, re.IGNORECASE)

    if match:
        return match.group()

    raise LookupError(f"Unable to find {needle} in manual.")


def format_func_name(name: str) -> str:
    # Read the text file
    current_dir = Path(__file__).parent
    manual = None
    with open(current_dir / "manual.txt", "r") as file:
        manual = file.read()

    if name not in original_cases:
        original_case = find_original_case(manual, name)
        original_cases[name] = original_case
        return original_case

    return original_cases[name]


def get_doc_url(name: str, type_: type):
    if isinstance(type_, Raster):
        name = f"RT_{name}"
    return f"https://postgis.net/docs/{name}.html"


functions_dict = {}


def parse_function_row(
    name: str, return_type_str: str, arg_types_str: str, description: str
) -> str:
    name = format_func_name(name)
    func = functions_dict.get(name, {})
    arg_types = parse_arg_types(arg_types_str)
    type_hint, inst = parse_return_type(return_type_str)
    if description is not None:
        description = description.replace('"', "'")
    func[arg_types] = {
        "type_hint": type_hint,
        "inst": inst,
        "description": description,
        "doc_url": get_doc_url(name, return_type),
    }
    functions_dict[name] = func


def format_function_row(name: str, func: dict):
    func_entries = []
    arg_template = Template(
        '($args):{"inst": $inst, "type_hint": $type_hint, "description": "$description", "doc_url": "$doc_url"}'  # noqa
    )
    for arg_tuple in func:
        args = ",".join(arg_tuple)
        if len(arg_tuple) == 1:
            args += ","
        formatted = arg_template.substitute(
            args=args,
            **func[arg_tuple],
        )
        func_entries.append(formatted)

    func_template = Template('"$name": {$entries}')
    return func_template.substitute(name=name, entries=",".join(func_entries))


def format_all_functions(functions: str):
    return black.format_str(functions, mode=black.Mode(line_length=100))


functions_rows = get_function_rows()
# Create the unformatted dictionary of all functions
for func in functions_rows:
    name, return_type, arg_types, description = func

    try:
        parse_function_row(name, return_type, arg_types, description)
    except LookupError:
        ...

# Sort functions in an OrderedDict
ordered_funcs = OrderedDict(sorted(functions_dict.items()))

# With all the functions populated in the dictionary, format them into strings
formatted_funcs = []
for name, func in ordered_funcs.items():
    formatted_funcs.append(format_function_row(name, func))


imports = """
"""
current_dir = Path(__file__).parent
functions_path = current_dir / "_functions.py"
module_template = Template(
    "from geoalchemy2.types import Geography, Geometry, GeomVal, Raster, SummaryStats\n"
    "from typing import Any, List\n"
    "_FUNCTIONS = {$functions}"
)

module_unformatted = module_template.substitute(functions=",".join(formatted_funcs))

functions_formatted = format_all_functions(module_unformatted)

with open(functions_path, "w") as file:
    file.write(functions_formatted)

# print(original_cases)
# print(all_return_types)
