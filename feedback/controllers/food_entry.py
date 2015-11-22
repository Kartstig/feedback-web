#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify
from flask.ext.login import login_user, current_user, logout_user
from feedback.services.FoodEntryService import FoodEntryService

food_entry = Blueprint('food_entry', __name__)

@food_entry.route('/api/food_entry/<int:id>', methods=['GET'])
def food_entry_get(id):
    return jsonify(FoodEntryService().filter_by(id=id).serialize())

@food_entry.route('/api/food_entry/all', methods=['GET'])
def food_entry_all():
    return jsonify(dict(food_entries=FoodEntryService().serialize()))

@food_entry.route('/api/food_entry/create', methods=['POST'])
def food_entry_create():
    errors = {}
    ps = FoodEntryService()
    if request.method == 'POST':
        try:
            p = ps.create(**request.form)
            return jsonify(p)
        except:
            return abort(500)
    else:
        return abort(401)
