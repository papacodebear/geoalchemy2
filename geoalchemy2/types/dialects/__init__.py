"""This module defines some dialect-specific functions used for Column types."""
from geoalchemy2.types.dialects import common
from geoalchemy2.types.dialects import mysql
from geoalchemy2.types.dialects import postgresql
from geoalchemy2.types.dialects import sqlite


def select_dialect(dialect_name):
    """Select the dialect from its name."""
    known_dialects = {
        "mysql": mysql,
        "postgresql": postgresql,
        "sqlite": sqlite,
    }
    return known_dialects.get(dialect_name, common)
