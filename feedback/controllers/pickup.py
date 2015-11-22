#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.PickupService import PickupService

pickup = Blueprint('pickup', __name__)

@pickup.route('/api/pickup/<int:id>', methods=['GET'])
def pickup_get(id):
    return jsonify(PickupService().filter_by(id=id).serialize())

@pickup.route('/api/pickup/all', methods=['GET'])
def pickup_all():
    return jsonify(dict(pickups=PickupService().serialize()))

@pickup.route('/api/pickup/create', methods=['POST'])
def pickup_create():
    errors = {}
    ps = PickupService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            return jsonify(p)
        except:
            return abort(500)
    else:
        return abort(401)
