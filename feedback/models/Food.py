#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from datetime import datetime

class Food(Base):

    __tablename__ = 'foods'

    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50), nullable=False)
    monetary_value      = Column(Integer)
    shelf_life          = Column(Integer)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, name, monetary_value=None, shelf_life=None):
        timestamp = datetime.now()
        self.name               = name
        self.monetary_value     = monetary_value
        self.shelf_life         = shelf_life
        self.created_at         = timestamp
        self.updated_at         = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
