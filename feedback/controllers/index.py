#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response
from flask.ext.login import current_user

from feedback.config import app_config
# from feedback.twilio.sms import SMS
from twilio import twiml

from random import choice
from feedback.stubs.volunteers import get_volunteers, get_donors, get_recipients

volunteers = get_volunteers()
donors = get_donors()
recipients = get_recipients()

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return render_template("index.html", current_user=current_user)

@index.route('/donate', methods=['GET', 'POST'])
def donate():
	if request.method == 'POST':
		# d = Donor(request.form['name'], request.form['location'], request.form['offering'])
		# d = donors[0]
		# donor_offerings = set(o.lower() for o in d.offering.split(', '))
		# for 
		# donor_offerings.intersect(set(o.lower() for o in r.need_profile.split(', ')))
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

@index.route('/about', methods=['GET'])
def about():
    return render_template("about.html", current_user=current_user)

@index.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", current_user=current_user)

@index.route('/respond', methods=['GET', 'POST'])
def respond():
	try:
		resp = twiml.Response()
		resp.message("I hear you, {}, you said {}".format(
			request.form.get('From', ''), request.form.get('Body', '')))
		return str(resp)
	except Exception as e:
		print e

@index.route('/map', methods=['GET'])
def map():
    return render_template('map.html',
        current_user=current_user,
        api_key=app_config.GOOGLE_API_KEY,
        active = request.form.get('active', ''))
