#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.Location import Location

class LocationService(Base):
    __model__ = Location
