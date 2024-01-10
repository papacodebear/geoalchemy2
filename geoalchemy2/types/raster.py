from geoalchemy2.comparator import BaseComparator
from geoalchemy2.elements import RasterElement
from geoalchemy2.types.gis_type import _GISType


class Raster(_GISType):
    """The Raster column type.

    Creating a raster column is done like this::

        Column(Raster)

    This class defines the ``result_processor`` method, so that raster values
    received from the database are converted to
    :class:`geoalchemy2.elements.RasterElement` objects.

    Args:
        spatial_index: Indicate if a spatial index should be created. Default is ``True``.
    """

    comparator_factory = BaseComparator
    """
    This is the way by which spatial operators and functions are
    defined for raster columns.
    """

    name = "raster"
    """ Type name used for defining raster columns in ``CREATE TABLE``. """

    from_text = "raster"
    """ The "from text" raster constructor. Used by the parent class'
        ``bind_expression`` method. """

    as_binary = "st_asbinary"
    """ The "as binary" function to use. Used by the parent class'
        ``column_expression`` method. """

    ElementType = RasterElement
    """ The element class to use. Used by the parent class'
        ``result_processor`` method. """

    cache_ok = False
    """ Disable cache for this type. """

    def __init__(self, spatial_index=True, from_text=None, name=None, nullable=True):
        # Enforce default values
        super(Raster, self).__init__(
            geometry_type=None,
            srid=-1,
            dimension=2,
            spatial_index=spatial_index,
            use_N_D_index=False,
            management=False,
            use_typmod=False,
            from_text=from_text,
            name=name,
            nullable=nullable,
        )
        self.extended = None

    @staticmethod
    def check_ctor_args(*args, **kwargs):
        return None, -1
