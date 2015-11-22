#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.FoodEntry import FoodEntry

class FoodEntryService(Base):
    __model__ = FoodEntry
