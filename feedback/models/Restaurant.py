#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Restaurant(Base):

    __tablename__ = 'restaurants'

    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50), nullable=False)
    phone_number        = Column(String(15))
    pickup_window       = Column(String(50))
    location_id         = Column(Integer, ForeignKey('locations.id'), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    admins = relationship("User",
        secondary="restaurant_admins",
        backref="restaurants")

    location = relationship("Location",
        foreign_keys="Restaurant.location_id",
        backref="restaurants")

    def __init__(self, name, location_id, phone_number=None, pickup_window=None):
        timestamp = datetime.now()
        self.name               = name
        self.location_id        = location_id
        self.phone_number       = phone_number
        self.created_at         = timestamp
        self.updated_at         = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
