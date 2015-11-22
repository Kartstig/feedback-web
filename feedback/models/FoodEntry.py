#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from datetime import datetime

class FoodEntry(Base):

    __tablename__ = 'food_entries'

    id                  = Column(Integer, primary_key=True)
    food_id             = Column(Integer, ForeignKey('foods.id'), nullable=False)
    pickup_id           = Column(Integer, ForeignKey('pickups.id'), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, food_id, pickup_id):
        timestamp = datetime.now()
        self.food_id            = food_id
        self.pickup_id          = pickup_id
        self.created_at         = timestamp
        self.updated_at         = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
