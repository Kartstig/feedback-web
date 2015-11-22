from sqlalchemy.ext.declarative import declarative_base as real_declarative_base

# Let's make this a class decorator
declarative_base = lambda cls: real_declarative_base(cls=cls)

@declarative_base
class Base(object):
    """
    Add some default properties and methods to the SQLAlchemy declarative base.
    """

    @property
    def columns(self):
        return [ c.name for c in self.__table__.columns ]

    @property
    def columnitems(self):
        return dict([ (c, getattr(self, c)) for c in self.columns ])

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems