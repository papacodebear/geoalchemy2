from sqlalchemy.dialects import postgresql
from sqlalchemy.types import Integer

from geoalchemy2.types import CompositeType
from geoalchemy2.types import Geometry


class GeometryDump(CompositeType):
    """The return type for functions like ``ST_Dump``.

    The type consists in a path and a geom field.
    You should normally never use this class directly.
    """

    typemap = {"path": postgresql.ARRAY(Integer), "geom": Geometry}
    """ Dictionary defining the contents of a ``geometry_dump``. """

    cache_ok = True
    """ Enable cache for this type. """
