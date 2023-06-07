"""This module defines some dialect-specific functions used for administration tasks."""
from geoalchemy2.admin.dialects import common
from geoalchemy2.admin.dialects import mysql
from geoalchemy2.admin.dialects import postgresql
from geoalchemy2.admin.dialects import sqlite


def select_dialect(dialect_name):
    """Select the dialect from its name."""
    known_dialects = {
        "mysql": mysql,
        "postgresql": postgresql,
        "sqlite": sqlite,
    }
    return known_dialects.get(dialect_name, common)
