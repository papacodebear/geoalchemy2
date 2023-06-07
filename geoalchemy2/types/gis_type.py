import warnings

from sqlalchemy.sql import func
from sqlalchemy.types import UserDefinedType

from geoalchemy2.comparator import Comparator
from geoalchemy2.exc import ArgumentError
from geoalchemy2.types.dialects import select_dialect


class _GISType(UserDefinedType):
    """The base class for spatial types.

    This class defines ``bind_expression`` and ``column_expression`` methods
    that wrap column expressions in ``ST_GeomFromEWKT``, ``ST_GeogFromText``,
    or ``ST_AsEWKB`` calls.

    This class also defines ``result_processor`` and ``bind_processor``
    methods. The function returned by ``result_processor`` converts WKB values
    received from the database to :class:`geoalchemy2.elements.WKBElement`
    objects. The function returned by ``bind_processor`` converts
    :class:`geoalchemy2.elements.WKTElement` objects to EWKT strings.

    Args:
        geometry_type: The geometry type.

            Possible values are:

              * ``"GEOMETRY"``,
              * ``"POINT"``,
              * ``"LINESTRING"``,
              * ``"POLYGON"``,
              * ``"MULTIPOINT"``,
              * ``"MULTILINESTRING"``,
              * ``"MULTIPOLYGON"``,
              * ``"GEOMETRYCOLLECTION"``,
              * ``"CURVE"``,
              * ``None``.

           The latter is actually not supported with
           :class:`geoalchemy2.types.Geography`.

           When set to ``None`` then no "geometry type" constraints will be
           attached to the geometry type declaration. Using ``None`` here
           is not compatible with setting ``management`` to ``True``.

           Default is ``"GEOMETRY"``.

        srid: The SRID for this column. E.g. 4326. Default is ``-1``.
        dimension: The dimension of the geometry. Default is ``2``.

            With ``management`` set to ``True``, that is when ``AddGeometryColumn`` is used
            to add the geometry column, there are two constraints:

            * The ``geometry_type`` must not end with ``"ZM"``.  This is due to PostGIS'
              ``AddGeometryColumn`` failing with ZM geometry types. Instead the "simple"
              geometry type (e.g. POINT rather POINTZM) should be used with ``dimension``
              set to ``4``.
            * When the ``geometry_type`` ends with ``"Z"`` or ``"M"`` then ``dimension``
              must be set to ``3``.

            With ``management`` set to ``False`` (the default) ``dimension`` is not
            taken into account, and the actual dimension is fully defined with the
            ``geometry_type``.

        spatial_index: Indicate if a spatial index should be created. Default is ``True``.
        use_N_D_index: Use the N-D index instead of the standard 2-D index.
        management: Indicate if the ``AddGeometryColumn`` and ``DropGeometryColumn``
            managements functions should be called when adding and dropping the
            geometry column. Should be set to ``True`` for PostGIS 1.x and SQLite. Default is
            ``False``. Note that this option has no effect for
            :class:`geoalchemy2.types.Geography`.
        use_typmod: By default PostgreSQL type modifiers are used to create the geometry
            column. To use check constraints instead set ``use_typmod`` to
            ``False``. By default this option is not included in the call to
            ``AddGeometryColumn``. Note that this option is only taken
            into account if ``management`` is set to ``True`` and is only available
            for PostGIS 2.x.
    """

    name = None
    """ Name used for defining the main geo type (geometry or geography)
        in CREATE TABLE statements. Set in subclasses. """

    from_text = None
    """ The name of "from text" function for this type.
        Set in subclasses. """

    as_binary = None
    """ The name of the "as binary" function for this type.
        Set in subclasses. """

    comparator_factory = Comparator
    """ This is the way by which spatial operators are defined for
        geometry/geography columns. """

    cache_ok = False
    """ Disable cache for this type. """

    def __init__(
        self,
        geometry_type="GEOMETRY",
        srid=-1,
        dimension=2,
        spatial_index=True,
        use_N_D_index=False,
        management=False,
        use_typmod=None,
        from_text=None,
        name=None,
        nullable=True,
        _spatial_index_reflected=None,
    ):
        geometry_type, srid = self.check_ctor_args(
            geometry_type, srid, dimension, management, use_typmod, nullable
        )
        self.geometry_type = geometry_type
        self.srid = srid
        if name is not None:
            self.name = name
        if from_text is not None:
            self.from_text = from_text
        self.dimension = dimension
        self.spatial_index = spatial_index
        self.use_N_D_index = use_N_D_index
        if management:
            warnings.warn(
                "The 'management' parameter is going to be deprecated and will raise an error in "
                "the version 0.14",
                PendingDeprecationWarning,
            )
        self.management = management
        self.use_typmod = use_typmod
        self.extended = self.as_binary == "ST_AsEWKB"
        self.nullable = nullable
        self._spatial_index_reflected = _spatial_index_reflected

    def get_col_spec(self):
        if not self.geometry_type:
            return self.name
        return "%s(%s,%d)" % (self.name, self.geometry_type, self.srid)

    def column_expression(self, col):
        """Specific column_expression that automatically adds a conversion function."""
        return getattr(func, self.as_binary)(col, type_=self)

    def result_processor(self, dialect, coltype):
        """Specific result_processor that automatically process spatial elements."""

        def process(value):
            if value is not None:
                kwargs = {}
                if self.srid > 0:
                    kwargs["srid"] = self.srid
                if self.extended is not None and dialect.name != "mysql":
                    kwargs["extended"] = self.extended
                return self.ElementType(value, **kwargs)

        return process

    def bind_expression(self, bindvalue):
        """Specific bind_expression that automatically adds a conversion function."""
        return getattr(func, self.from_text)(bindvalue, type_=self)

    def bind_processor(self, dialect):
        """Specific bind_processor that automatically process spatial elements."""

        def process(bindvalue):
            return select_dialect(dialect.name).bind_processor_process(self, bindvalue)

        return process

    @staticmethod
    def check_ctor_args(geometry_type, srid, dimension, management, use_typmod, nullable):
        try:
            srid = int(srid)
        except ValueError:
            raise ArgumentError("srid must be convertible to an integer")
        if geometry_type:
            geometry_type = geometry_type.upper()
            if management:
                if geometry_type.endswith("ZM"):
                    # PostGIS' AddGeometryColumn does not work with ZM geometry types. Instead
                    # the simple geometry type (e.g. POINT rather POINTZM) should be used with
                    # dimension set to 4
                    raise ArgumentError(
                        "with management=True use geometry_type={!r} and "
                        "dimension=4 for {!r} geometries".format(geometry_type[:-2], geometry_type)
                    )
                elif geometry_type[-1] in ("Z", "M") and dimension != 3:
                    # If a Z or M geometry type is used then dimension must be set to 3
                    raise ArgumentError(
                        "with management=True dimension must be 3 for "
                        "{!r} geometries".format(geometry_type)
                    )
        else:
            if management:
                raise ArgumentError("geometry_type set to None not compatible with management")
            if srid > 0:
                warnings.warn("srid not enforced when geometry_type is None")

        if use_typmod and not management:
            warnings.warn("use_typmod ignored when management is False")
        if use_typmod is not None and not nullable:
            raise ArgumentError(
                'The "nullable" and "use_typmod" arguments can not be used together'
            )

        return geometry_type, srid
