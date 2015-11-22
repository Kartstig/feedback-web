#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response
from flask.ext.login import current_user

from feedback.config import app_config

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return render_template("index.html", current_user=current_user)

@index.route('/about', methods=['GET'])
def about():
    return render_template("about.html", current_user=current_user)

@index.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", current_user=current_user)