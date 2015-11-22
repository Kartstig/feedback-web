#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.LocationService import LocationService

location = Blueprint('location', __name__)

@location.route('/api/location/<int:id>', methods=['GET'])
def location_get(id):
    return jsonify(LocationService().filter_by(id=id).serialize())

@location.route('/api/location/all', methods=['GET'])
def location_all():
    return jsonify(dict(locations=LocationService().serialize()))

@location.route('/api/location/create', methods=['POST'])
def location_create():
    errors = {}
    ps = LocationService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            return jsonify(p)
        except:
            return abort(500)
    else:
        return abort(401)
