#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from feedback.models.Restaurant import Restaurant

class Pickup(Base):

    __tablename__ = 'pickups'

    id                  = Column(Integer, primary_key=True)
    restaurant_id       = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    courier_id          = Column(Integer, ForeignKey('users.id'))
    recipient_id        = Column(Integer, ForeignKey('users.id'))
    pickup_time         = Column(DateTime, nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    restaurant = relationship(Restaurant,
        foreign_keys="Pickup.restaurant_id",
        backref="pickups")

    courier = relationship("User",
        foreign_keys="Pickup.courier_id",
        backref="pickups")

    recipient = relationship("User",
        foreign_keys="Pickup.recipient_id",
        backref="deliveries")

    def __init__(self, restaurant_id, pickup_time, \
            courier_id=None, recipient_id=None):
        timestamp = datetime.now()
        self.restaurant_id      = restaurant_id
        self.pickup_time        = pickup_time
        self.courier_id         = courier_id
        self.recipient_id       = recipient_id
        self.created_at         = timestamp
        self.updated_at         = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
