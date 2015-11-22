#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response
from flask.ext.login import current_user

from feedback.config import app_config
# from feedback.twilio.sms import SMS
from twilio import twiml

from random import choice
from feedback.stubs import get_volunteers

volunteers = get_volunteers()

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return render_template("index.html", current_user=current_user)

@index.route('/donate', methods=['GET', 'POST'])
def donate():
	if request.method == 'POST':
		pass
	else:
		return render_template("donate.html", current_user=current_user)

def handle_donation(donor):
	resp = twiml.Response()
	volunteer = choice(volunteers)
	sms = SMS()
	# TODO: make second param a google link?
	sms.send_msg(volunteer.mobile, 
		"A food pickup is ready for you at {} ({})".format(
			donor.name, donor.location))


@index.route('/respond', methods=['GET', 'POST'])
def respond():
	try:
		resp = twiml.Response()
		resp.message("I hear you, {}, you said {}".format(
			request.form.get('From', ''), request.form.get('Body', '')))
		return str(resp)
	except Exception as e:
		print e
