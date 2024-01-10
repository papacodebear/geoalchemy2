from sqlalchemy.types import Float

from geoalchemy2.types import CompositeType
from geoalchemy2.types.geometry import Geometry


class GeomVal(CompositeType):
    """Define the GeomVal data type.

    geomval is a compound data type consisting of a geometry object referenced by the .geom
    field and val, a double precision value that represents the pixel value at a particular
    geometric location in a raster band. It is used by the ST_DumpAsPolygon and Raster intersection
    family of functions as an output type to explode a raster band into geometry polygons.
    """

    typemap = {
        "geom": Geometry,
        "val": Float,
    }

    cache_ok = True
    """ Enable cache for this type. """
