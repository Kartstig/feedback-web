#!/usr/bin/ python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

from feedback import db
from feedback.config import app_config
from feedback.models.Base import Base
from feedback.models.User import User
from feedback.models.Location import Location
from feedback.models.Restaurant import Restaurant
from feedback.models.Pickup import Pickup
from feedback.models.Food import Food

from feedback.services.LocationService import LocationService
from feedback.services.RestaurantService import RestaurantService
from feedback.services.PickupService import PickupService
from feedback.services.FoodService import FoodService

def new_schema():
    Base.metadata.drop_all(db.engine)
    Base.metadata.create_all(db.engine)

def drop_schema():
    Base.metadata.drop_all(db.engine)

def bootstrap_data():
    foods = [
        {
            "name":             "haddock",
            "monetary_value":   800,
            "shelf_life":       2
        },
        {
            "name":             "cod",
            "monetary_value":   1000,
            "shelf_life":       2
        },
        {
            "name":             "foie gras",
            "monetary_value":   900,
            "shelf_life":       2
        },
        {
            "name":             "donuts",
            "monetary_value":   80,
            "shelf_life":       4
        },
        {
            "name":             "milk",
            "monetary_value":   100,
            "shelf_life":       10
        },
        {
            "name":             "eggs",
            "monetary_value":   220,
            "shelf_life":       12
        },
        {
            "name":             "quaaludes",
            "monetary_value":   90000,
            "shelf_life":       99
        }
    ]
    add_objects(foods, Food)

    locations = [
        {
            "street_address":   "2138 Triad Court",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43235"
        },
        {
            "street_address":   "5830 Godown Rd",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43235"  
        },
        {
            "street_address":   "1092 Bethel Rd",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43220"  
        },
        {
            "street_address":   "2754 N High St",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43214"  
        },
        {
            "street_address":   "3720 W Dublin Granville Rd",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43235"  
        },
        {
            "street_address":   "4590 Shires Ct",
            "city":             "Columbus",
            "state":            "OH",
            "zip_code":         "43220"
        }
    ]
    add_objects(locations, Location)

    restaurants = [
        {
            "name":             "Refectory Restaurant & Bistro",
            "phone_number":     6144519772,
            "pickup_window":    "(M,9-5),(T,9-5)",
            "location_id":      LocationService().get(3).id
        },
        {
            "name":             "Tim Hortons",
            "phone_number":     6144519772,
            "pickup_window":    "(W,9-5),(Th,9-5)",
            "location_id":      LocationService().get(4).id
        },
        {
            "name":             "Joe's Crab Shack",
            "phone_number":     6147996106,
            "pickup_window":    "(W,9-5),(F,9-5)",
            "location_id":      LocationService().get(5).id
        }
    ]
    add_objects(restaurants, Restaurant)

    users = [
        {
            "username":     "kartstig@gmail.com",
            "first_name":   "Herman",
            "last_name":    "Singh",
            "password":     "password",
            "phone_number": "4435107985",
            "role":         "user,admin,volunteer,recipient",
            "location_id":  LocationService().get(1).id
        },
        {
            "username":     "aslan235@gmail.com",
            "first_name":   "Scoot",
            "last_name":    "Ziegler",
            "password":     "password",
            "phone_number": "4192831501",
            "role":         "user,admin,volunteer,recipient",
            "location_id":  LocationService().get(2).id
        },
        {
            "username":     "r1@feedback.com",
            "first_name":   "Uncle",
            "last_name":    "Fester",
            "phone_number": "",
            "role":         "user,recipient",
            "location_id":  LocationService().get(6).id,
            "interests":    "donuts,milk,eggs,cod"
        }
    ]
    add_objects(users, User)

    pickups = [
        {
            "restaurant_id":    RestaurantService().get(1).id,
            "pickup_time":      datetime.now()
        }
    ]
    add_objects(pickups, Pickup)

    p = PickupService().get(1)
    f1 = FoodService().get(1)
    f2 = FoodService().get(2)
    p.foods.append(f1)
    p.foods.append(f2)
    db.session.add(p)
    db.session.commit()

def geocode(addr, city, state, zip):
    data = [addr, city, state, zip]
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
    r = requests.get(url.format( \
        ",".join(map(lambda x: x.replace(" ", "+"), data)), \
        app_config.GOOGLE_API_KEY), verify=False)
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
