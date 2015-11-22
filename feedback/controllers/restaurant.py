#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify, abort
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.RestaurantService import RestaurantService

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/api/restaurant/<int:id>', methods=['GET'])
def restaurant_get(id):
    return jsonify(RestaurantService().filter_by(id=id).serialize())

@restaurant.route('/api/restaurant/all', methods=['GET'])
def restaurant_all():
    return jsonify(dict(restaurants=RestaurantService().serialize()))

@restaurant.route('/api/restaurant/create', methods=['POST'])
def restaurant_create():
    errors = {}
    ps = RestaurantService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            if p:
                return jsonify(p.tojson())
        except:
            return abort(500)
    else:
        return abort(401)
