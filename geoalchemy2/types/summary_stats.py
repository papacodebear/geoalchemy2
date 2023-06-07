from sqlalchemy.types import Float
from sqlalchemy.types import Integer

from geoalchemy2.types import CompositeType


class SummaryStats(CompositeType):
    """Define the composite type returned by the function ST_SummaryStatsAgg."""

    typemap = {
        "count": Integer,
        "sum": Float,
        "mean": Float,
        "stddev": Float,
        "min": Float,
        "max": Float,
    }

    cache_ok = True
    """ Enable cache for this type. """
