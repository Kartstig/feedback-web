#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.Food import Food

class FoodService(Base):
    __model__ = Food
