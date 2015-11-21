#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, jsonify

from feedback.models.User import User
from feedback.services.UserService import UserService

user = Blueprint('user', __name__)

@user.route('/api/user/<int:id>', methods=['GET'])
def user_get(id):
    return jsonify(UserService().filter_by(id=id).serialize())
