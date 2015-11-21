#!/usr/bin/ python
# -*- coding: utf-8 -*-

from feedback.services.Base import Base
from feedback.models.User import User

class UserService(Base):
    __model__ = User

    def by_username(self, username):
        try:
            return self.session.query(User).filter_by(username=username).one()
        except:
            return None
