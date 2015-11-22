#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.Restaurant import Restaurant

class RestaurantService(Base):
    __model__ = Restaurant
