from sqlalchemy.types import UserDefinedType

from geoalchemy2.elements import CompositeElement


class CompositeType(UserDefinedType):
    """A composite type used by some spatial functions.

    A wrapper for :class:`geoalchemy2.elements.CompositeElement`, that can be
    used as the return type in PostgreSQL functions that return composite
    values.

    This is used as the base class of :class:`geoalchemy2.types.GeometryDump`.
    """

    typemap = {}
    """ Dictionary used for defining the content types and their
        corresponding keys. Set in subclasses. """

    class comparator_factory(UserDefinedType.Comparator):
        def __getattr__(self, key):
            try:
                type_ = self.type.typemap[key]
            except KeyError:
                raise AttributeError("Type '%s' doesn't have an attribute: '%s'" % (self.type, key))

            return CompositeElement(self.expr, key, type_)
