#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import request, redirect, url_for, current_app, \
    render_template, flash, Blueprint, Response, session
from flask.ext.login import current_user

from feedback.config import app_config
# from feedback.twilio.sms import SMS
from twilio import twiml

from random import choice, randint
from feedback.stubs.volunteers import get_volunteers, get_donors, get_recipients

volunteers = get_volunteers()
donors = get_donors()
recipients = get_recipients()

invitations = {}
declined = {}
deliveries = {}

def generate_invitation_id():
	return "".join(str(randint(0,9)) for i in xrange(0,4))

def get_invitation_id():
	new_id = generate_invitation_id()
	while new_id in invitations:
		new_id = generate_invitation_id()
	return new_id

def choose_volunteer():
	volunteer = choice(volunteers)
	while volunteer.mobile in invitations or volunteer.mobile in declined:
		volunteer = choice(volunteers)
	return volunteer

def normalize_foodlist(foodlist):
	return set(o.lower() for o in r.foodlist.split(', '))

def find_match(donor, recipients):
	donor_offerings = normalize_foodlist(donor.offering)
	for r in recipients:
		need_profile = normalize_foodlist(r.need_profile)
		if donor_offerings & need_profile:
			return r

index = Blueprint('index', __name__)

@index.route('/', methods=['GET'])
def main():
    return render_template("index.html", current_user=current_user)

@index.route('/donate', methods=['GET', 'POST'])
def donate():
	if request.method == 'POST':
		# d = Donor(request.form['name'], request.form['location'], request.form['offering'])
		d = donors[0]
		target_recipient = find_match(d, recipients)
		handle_donation(d, target_recipient)
	else:
		return render_template("donate.html", current_user=current_user)

def invite_volunteer(donor, recipient):
	volunteer = choose_volunteer()
	invitations[volunteer.mobile] = (donor, recipient)
	return volunteer

def handle_donation(donor, recipient):
	resp = twiml.Response()
	volunteer = invite_volunteer(donor, recipient)

	sms = SMS()
	# TODO: make second param a google link?
	sms.send_msg(volunteer.mobile,
		"A food pickup is ready for you at {} ({}). Text 'Yes' to accept this mission, or 'No' to decline.".format(
			donor.name, donor.location))

@index.route('/about', methods=['GET'])
def about():
    return render_template("about.html", current_user=current_user)

@index.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", current_user=current_user)

def debug(resp):
	resp.message("I hear you, {}, you said {}".format(
		request.form.get('From', ''), request.form.get('Body', '')))

@index.route('/respond', methods=['GET', 'POST'])
def respond():
	try:
		resp = twiml.Response()

		from_number = request.form.get('From', '')
		body = request.form.get('Body', '')
		if 'in-delivery' in session:
			# send two messages to both
			
			# clean up state
			pass
		# volunteer is at picking up stage
		elif 'claimed' in session:
			(donor, recipient) = deliveries[body] = invitations[from_number]
			resp.message("Please deliver the parcel to {}, and text 'done' when delivered.".format(recipient.location))
			session['in-delivery'] = true
		elif from_number in invitations:
			if 'n' in body.lower():
				# remove from invitations
				invite = invitations.pop(from_number)
				declined[from_number] = true
				# re-invite next volunteer
				handle_donation(*invite)
			else:
				session['claimed'] = from_number
				resp.message("Wonderful! When you pickup the parcel, text 'pickup' back to us, and we'll let them know you are coming!".format(body))
	
		# debug(resp)
		return str(resp)
	except Exception as e:
		print e

@index.route('/map', methods=['GET'])
def map():
    return render_template('map.html',
        current_user=current_user,
        api_key=app_config.GOOGLE_API_KEY,
        active = request.form.get('active', ''))
