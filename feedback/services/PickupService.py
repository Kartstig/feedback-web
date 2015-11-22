#!/usr/bin/ python
# -*- coding: utf-8 -*-

from sqlalchemy import text

from feedback.services.Base import Base
from feedback.models.Pickup import Pickup
from feedback.models.User import User

class PickupService(Base):
    __model__ = Pickup

    def available_pickups(self):
        return self.session.query(Pickup).filter(Pickup.courier_id.is_(None)).all()
