#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.Pickup import Pickup

class PickupService(Base):
    __model__ = Pickup