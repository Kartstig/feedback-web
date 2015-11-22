#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify, abort
from flask.ext.login import login_user, current_user, logout_user
from feedback.models.User import User
from feedback.services.UserService import UserService

user = Blueprint('user', __name__)

@user.route('/api/user/<int:id>', methods=['GET'])
def user_get(id):
    return jsonify(UserService().filter_by(id=id).serialize())

@user.route('/api/user/all', methods=['GET'])
def user_all():
    return jsonify(dict(users=UserService().serialize()))

@user.route('/api/user/create', methods=['POST'])
def user_create():
    errors = {}
    us = UserService()
    if request.method == 'POST':
        try:
            u = us.create(**request.form)
            if u:
                return jsonify(u.tojson())
        except:
            return abort(500)
    else:
        return abort(401)


@user.route('/login', methods=['POST'])
def user_login():
    errors = {}
    us = UserService()
    if request.method == 'POST':
        try:
            user = us.by_username(request.form['username'])
            if user.valid_password(request.form['password']):
                return jsonify(user)
            else:
                return abort(401)
        except:
            return abort(500)
    else:
        return abort(400)
