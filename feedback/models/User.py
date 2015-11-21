#!/usr/bin/ python
# -*- coding: utf-8 -*-

import re, os
from Base import Base
from bcrypt import hashpw, gensalt
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from datetime import datetime
from flask.ext.login import UserMixin

__roles__ = ('user', 'admin')

class User(Base, UserMixin):

    __tablename__ = 'users'

    id                  = Column(Integer, primary_key=True)
    username            = Column(String(50), unique=True, nullable=False)
    password            = Column(String(60))
    first_name          = Column(String(50))
    last_name           = Column(String(50))
    phone_number        = Column(String(15))
    role                = Column(Enum(*__roles__), default='user', nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    validation_token    = Column(String(64))
    last_login          = Column(DateTime)

    def __init__(self, username, password=None, first_name=None, last_name=None, 
                 phone_number=None, role='user', last_login=None):
        timestamp = datetime.now()
        self.username           = username
        self.password           = (self.pass_hash(password)) if password else None
        self.first_name         = first_name
        self.last_name          = last_name
        self.phone_number       = self.parse_phone(phone_number)
        self.role               = role
        self.created_at         = timestamp
        self.updated_at         = timestamp
        self.validation_token   = os.urandom(32).encode('hex')
        self.last_login         = last_login

    @staticmethod
    def pass_hash(password):
        return hashpw(password.encode('utf-8'), gensalt())

    @staticmethod
    def parse_phone(phone_number):
        if phone_number:
            return re.compile(r'[^\d]+').sub('', phone_number)
        else:
            return None

    def valid_password(self, attempt):
        return (self.password 
            and hashpw(attempt.encode('utf-8'), self.password.encode('utf-8')) == self.password)

    def phone_formatter(self, fmt="{}.{}.{}"):
        if not self.phone_number:
            return ""
        elif fmt is None:
            return self.phone_number
        segments = (self.phone_number[0:3], self.phone_number[3:6], self.phone_number[6:])
        return fmt.format(*segments)

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.username)
