#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response
from flask.ext.login import current_user

from feedback.config import app_config
# from feedback.twilio.sms import SMS
from twilio import twiml

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return render_template("index.html", current_user=current_user)

@index.route('/respond', methods=['GET', 'POST'])
def respond():
	try:
		# sms = SMS()
		# (from_number, msg) = sms.receive_msg(request)
		# sms.send_msg(from_number, 
		# 	"I hear you, {}, you said {}".format(from_number, msg))
		resp = twiml.Response("I hear you, {}, you said {}".format(
			request.form.get('From', ''), request.form.get('Body', '')))
		resp.message()
		return str(resp)
	except Exception as e:
		print e
