#!/usr/bin/ python
# -*- coding: utf-8 -*-

import datetime
import calendar
from sqlalchemy import Date, and_, desc, asc, func
from datetime import date
from feedback import db
from sqlalchemy.orm import class_mapper

class Base(object):
    __model__ = None
    __restricted_cols__ = []

    def __init__(self):
        self.session = db.session
        self.session.rollback()
        self.query = db.session.query(self.__model__)
        self._columns = [c.key for c in class_mapper(self.__model__).columns]

    def columns(self):
        return [c for c in self._columns if c not in self.__restricted_cols__]

    def is_instance(self, model):
        return isinstance(model, self.__model__)

    def get(self, id):
        """
        Find a single record by its id.
        """
        try:
            return self.session.query(self.__model__).filter_by(id=id).one()
        except:
            return None

    def all(self):
        """
        This will return ALL records.
        Use with caution
        """
        return self.query.all()

    def order_by(col, order="desc"):
        if order == "asc":
            self.query = self.query.order_by(asc(col))
        elif order == "desc":
            self.query = self.query.order_by(desc(col))
        return self

    def new(self, **kwargs):
        """
        Invoke the model constructor.
        Returns the model or None
        """
        try:
            return self.__model__(**kwargs)
        except:
            None

    def create(self, **kwargs):
        """
        Creates a model and saves
        commits it to the session
        """
        try:
            obj = self.__model__(**kwargs)
            self.save(obj)
            return obj
        except:
            return False

    def save(self, model):
        """
        Takes a model as an argument
        and commits it to the session
        """
        try:
            self.session.add(model)
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def delete(self, model):
        """
        Takes a model and removes it
        """
        try:
            self.session.delete(model)
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def serialize(self):
        """
        Return a serialized dict so
        it can be dumped into a JSON
        object
        """
        try:
            results = self.query.all()
            if len(results) > 1:
                return [ dict((c, getattr(item, c)) for c in self.columns()) \
                    for item in results ]
            elif results:
                return dict((c, getattr(results[0], c)) for c in self.columns())
            else:
                return {}
        except:
            raise

    def filter_by(self, **kwargs):
        """
        Filter a query by list of
        keyword arguments
        """
        self.query = self.query.filter_by(**kwargs)
        return self

    def group_by_month(self, month, year):
        """
        Take a month,year and return
        records within that time
        """
        num_days = calendar.monthrange(year, month)[1]
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month, num_days)
        self.query = self.query.filter(self.__model__.created_at.between(start_date, end_date))
        return self

    def group_by_year(self, year):
        """
        Take a year and return
        records within that time
        """
        start_date = '{}-01-01'.format(year)
        end_date = '{}-12-31'.format(year)
        self.query = self.query.filter(self.__model__.created_at.between(start_date, end_date))
        return self

    def paginate(self, page=1, page_size=100):
        """
        Takes a query and returns
        a paged result set
        (query, page_count, start, end)
        """
        if page > 0:
            count = self.query.count()
            page_count = count/page_size if count%page_size == 0 else count/page_size+1
            if page_count <= 10 :
                start = 1
                end = page_count+1
            elif page_count > 10:
                if page <= 6:
                    start = 1
                    end = 11
                elif page > 6:
                    max_page = min(page+4, page_count)
                    start = max_page-9
                    end = max_page+1
            return (self.query.offset((page-1)*page_size).limit(page_size).all(), page_count, start, end)
        else:
            return ()
