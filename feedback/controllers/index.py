#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response

from feedback.config import app_config

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return "Hello"
