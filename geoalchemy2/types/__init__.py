"""This module aggregates Column types.

The :class:`geoalchemy2.types.Geometry`, :class:`geoalchemy2.types.Geography`, and
:class:`geoalchemy2.types.Raster` classes are used when defining geometry, geography and raster
columns/properties in models.
"""


from sqlalchemy.dialects.postgresql.base import ischema_names as _postgresql_ischema_names
from sqlalchemy.dialects.sqlite.base import ischema_names as _sqlite_ischema_names
from sqlalchemy.ext.compiler import compiles

from geoalchemy2.types.composite_type import CompositeType
from geoalchemy2.types.dialects import select_dialect
from geoalchemy2.types.dummy_geometry import _DummyGeometry
from geoalchemy2.types.geography import Geography
from geoalchemy2.types.geometry import Geometry
from geoalchemy2.types.gis_type import _GISType
from geoalchemy2.types.raster import Raster


@compiles(_GISType, "mysql")
def get_col_spec(self, *args, **kwargs):
    if self.geometry_type is not None:
        spec = "%s" % self.geometry_type
    else:
        spec = "GEOMETRY"

    if not self.nullable or self.spatial_index:
        spec += " NOT NULL"
    if self.srid > 0:
        spec += " SRID %d" % self.srid
    return spec


# Register Geometry, Geography and Raster to SQLAlchemy's reflection subsystems.
_postgresql_ischema_names["geometry"] = Geometry
_postgresql_ischema_names["geography"] = Geography
_postgresql_ischema_names["raster"] = Raster

_sqlite_ischema_names["GEOMETRY"] = Geometry
_sqlite_ischema_names["POINT"] = Geometry
_sqlite_ischema_names["LINESTRING"] = Geometry
_sqlite_ischema_names["POLYGON"] = Geometry
_sqlite_ischema_names["MULTIPOINT"] = Geometry
_sqlite_ischema_names["MULTILINESTRING"] = Geometry
_sqlite_ischema_names["MULTIPOLYGON"] = Geometry
_sqlite_ischema_names["CURVE"] = Geometry
_sqlite_ischema_names["GEOMETRYCOLLECTION"] = Geometry
_sqlite_ischema_names["RASTER"] = Raster


__all__ = [
    "_GISType",
    "CompositeType",
    "_DummyGeometry",
    "Geography",
    "Geometry",
    "GeometryDump",
    "Raster",
    "SummaryStats",
    "dialects",
    "select_dialect",
]


def __dir__():
    return __all__
