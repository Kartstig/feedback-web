#!/usr/bin/ python
# -*- coding: utf-8 -*-

import requests

from feedback import db
from feedback.config import app_config
from feedback.models.Base import Base
from feedback.models.User import User
from feedback.models.Location import Location
from feedback.models.Restaurant import Restaurant
from feedback.models.Pickup import Pickup
from feedback.models.Food import Food
from feedback.models.FoodEntry import FoodEntry

def new_schema():
    Base.metadata.drop_all(db.engine)
    Base.metadata.create_all(db.engine)

def drop_schema():
    Base.metadata.drop_all(db.engine)

def bootstrap_data():
    users = [
        {
            "username":     "user01@test.com",
            "first_name":   "Robot",
            "last_name":    "1",
            "password":     "1234",
            "phone_number": "",
            "role":         "admin"
        },
        {
            "username":     "user02@test.com",
            "first_name":   "Robot",
            "last_name":    "2",
            "password":     "5678",
            "phone_number": "",
            "role":         "user"
        },
        {
            "username":     "user03@test.com",
            "first_name":   "Robot",
            "last_name":    "3",
            "phone_number": "",
            "role":         "user"
        }
    ]

    add_objects(users, User)

def geocode(addr, city, state, zip):
    data = [addr, city, state, zip]
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
    r = requests.get(url.format( \
        ",".join(map(lambda x: x.replace(" ", "+"), data)), \
        app_config.GOOGLE_API_KEY))
    results = r.json()
    return (results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng'])

def add_objects(input_array, obj):
    try:
        print "Building {}...".format(obj.__tablename__)
        for l in input_array:
            db.session.add(obj(**l))
        print "Done"
    except:
        print "Failed"
    finally:
        db.session.commit()

if __name__ == '__main__':
        pass
