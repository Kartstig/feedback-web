#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class RestaurantAdmin(Base):

    __tablename__ = 'restaurant_admins'

    id                  = Column(Integer, primary_key=True)
    restaurant_id       = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    admin               = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, restaurant_id, admin):
        timestamp = datetime.now()
        self.restaurant_id      = restaurant_id
        self.admin              = admin
        self.created_at         = timestamp
        self.updated_at         = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
