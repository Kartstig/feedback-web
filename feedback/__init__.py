#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from feedback.config import app_config

app = Flask(__name__)
app.config.from_object(app_config)
db = SQLAlchemy(app=app)

def create_app():
    from feedback.controllers.index import index
    from feedback.controllers.user import user
    from feedback.controllers.pickup import pickup
    from feedback.controllers.food import food
    from feedback.controllers.location import location
    from feedback.controllers.restaurant import restaurant
    app.register_blueprint(index)
    app.register_blueprint(user)
    app.register_blueprint(pickup)
    app.register_blueprint(food)
    app.register_blueprint(location)
    app.register_blueprint(restaurant)

    return app