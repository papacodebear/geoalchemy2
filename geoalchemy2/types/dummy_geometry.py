from geoalchemy2.types.geometry import Geometry


class _DummyGeometry(Geometry):
    """A dummy type only used with SQLite."""

    def get_col_spec(self):
        return "GEOMETRY"
