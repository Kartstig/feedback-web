#!/usr/bin/ python
# -*- coding: utf-8 -*-

import requests

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from datetime import datetime

class Location(Base):

    __tablename__ = 'locations'

    id                  = Column(Integer, primary_key=True)
    street_address      = Column(String(50), nullable=False)
    city                = Column(String(50), nullable=False)
    state               = Column(String(50), nullable=False)
    zip_code            = Column(Integer, nullable=False)
    lat                 = Column(Float)
    lng                 = Column(Float)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, street_address, city, state, zip_code):
        timestamp = datetime.now()
        self.street_address     = street_address
        self.city               = city
        self.state              = state
        self.zip_code           = zip_code
        self.created_at         = timestamp
        self.updated_at         = timestamp

        # Get Lat Long from Google
        (self.lat, self.lng) = \
            geocoder(self.street_address, self.city, self.state, self.zip_code)

    @staticmethod
    def geocoder(addr, city, state, zip):
        data = [addr, city, state, zip]
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
        try:
            r = requests.get(url.format( \
                ",".join(map(lambda x: x.replace(" ", "+"), data)), \
                app_config.GOOGLE_API_KEY)).json()
            return (r['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng'])
        except:
            return (None, None)

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
