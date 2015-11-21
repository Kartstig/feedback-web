#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from feedback.config import app_config

app = Flask(__name__)
app.config.from_object(app_config)
db = SQLAlchemy(app=app)

def create_app():
    from feedback.controllers.index import index
    from feedback.controllers.user import user
    app.register_blueprint(index)
    app.register_blueprint(user)

    return app