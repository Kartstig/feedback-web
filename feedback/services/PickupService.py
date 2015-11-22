#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.Pickup import Pickup
from feedback.models.User import User

class PickupService(Base):
    __model__ = Pickup
