from geoalchemy2.elements import WKBElement
from geoalchemy2.types import _GISType


class Geometry(_GISType):
    """The Geometry type.

    Creating a geometry column is done like this::

        Column(Geometry(geometry_type='POINT', srid=4326))

    See :class:`geoalchemy2.types._GISType` for the list of arguments that can
    be passed to the constructor.

    If ``srid`` is set then the ``WKBElement`` objects resulting from queries will
    have that SRID, and, when constructing the ``WKBElement`` objects, the SRID
    won't be read from the data returned by the database. If ``srid`` is not set
    (meaning it's ``-1``) then the SRID set in ``WKBElement`` objects will be read
    from the data returned by the database.
    """

    name = "geometry"
    """ Type name used for defining geometry columns in ``CREATE TABLE``. """

    from_text = "ST_GeomFromEWKT"
    """ The "from text" geometry constructor. Used by the parent class'
        ``bind_expression`` method. """

    as_binary = "ST_AsEWKB"
    """ The "as binary" function to use. Used by the parent class'
        ``column_expression`` method. """

    ElementType = WKBElement
    """ The element class to use. Used by the parent class'
        ``result_processor`` method. """

    cache_ok = False
    """ Disable cache for this type. """
