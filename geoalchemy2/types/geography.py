from geoalchemy2.elements import WKBElement
from geoalchemy2.types import _GISType


class Geography(_GISType):
    """The Geography type.

    Creating a geography column is done like this::

        Column(Geography(geometry_type='POINT', srid=4326))

    See :class:`geoalchemy2.types._GISType` for the list of arguments that can
    be passed to the constructor.
    """

    name = "geography"
    """ Type name used for defining geography columns in ``CREATE TABLE``. """

    from_text = "ST_GeogFromText"
    """ The ``FromText`` geography constructor. Used by the parent class'
        ``bind_expression`` method. """

    as_binary = "ST_AsBinary"
    """ The "as binary" function to use. Used by the parent class'
        ``column_expression`` method. """

    ElementType = WKBElement
    """ The element class to use. Used by the parent class'
        ``result_processor`` method. """

    cache_ok = False
    """ Disable cache for this type. """
