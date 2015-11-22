#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify, abort
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.LocationService import LocationService
from feedback.services.UserService import UserService
from feedback.services.RestaurantService import RestaurantService

location = Blueprint('location', __name__)

@location.route('/api/location/<int:id>', methods=['GET'])
def location_get(id):
    return jsonify(LocationService().filter_by(id=id).serialize())

@location.route('/api/location/restaurants', methods=['GET'])
def location_restaurant():
    restaurants = RestaurantService().all()
    return jsonify(locations=[r.location.tojson() for r in restaurants])

@location.route('/api/location/recipients', methods=['GET'])
def location_recipient():
    users = UserService().by_role("recipient")
    if users:
        return jsonify(dict(locations=[u.location.tojson() for u in users]))
    else:
        return jsonify(dict(locations=[]))

@location.route('/api/location/create', methods=['POST'])
def location_create():
    errors = {}
    ps = LocationService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            if p:
                return jsonify(p.tojson())
        except:
            return abort(500)
    else:
        return abort(401)
