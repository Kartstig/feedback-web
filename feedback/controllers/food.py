#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify, abort
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.FoodService import FoodService

food = Blueprint('food', __name__)

@food.route('/api/food/<int:id>', methods=['GET'])
def food_get(id):
    return jsonify(FoodService().filter_by(id=id).serialize())

@food.route('/api/food/all', methods=['GET'])
def food_all():
    return jsonify(dict(food_entries=FoodService().serialize()))

@food.route('/api/food/create', methods=['POST'])
def food_create():
    errors = {}
    ps = FoodService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            if p:
                return jsonify(p.tojson())
        except:
            return abort(500)
    else:
        return abort(401)
