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

volunteer_map = dict((v.mobile, v) for v in volunteers)

# stores the v.mobile: -> (donor, recipient) for invited volunteers
invitations = {}
# stores the v.mobile: -> True for invited volunteers
declined = {}
# stores the v.mobile: -> (donor, recipient) for deliveries-in-progress
deliveries = {}

# def generate_invitation_id():
# 	return "".join(str(randint(0,9)) for i in xrange(0,4))

# def get_invitation_id():
# 	new_id = generate_invitation_id()
# 	while new_id in invitations:
# 		new_id = generate_invitation_id()
# 	return new_id

def normalize_foodlist(foodlist):
	"""returns lower-case list of tokens from comma-sep string"""
	return set(o.lower() for o in r.foodlist.split(', '))

def find_match(donor, recipients):
	"""finds first recipient matching the donor profile"""
	donor_offerings = normalize_foodlist(donor.offering)
	for r in recipients:
		need_profile = normalize_foodlist(r.need_profile)
		if donor_offerings & need_profile:
			return r

def choose_volunteer():
	"""chooses a volunteer not already active or declined"""
	volunteer = choice(volunteers)
	while volunteer.mobile in invitations or volunteer.mobile in declined:
		volunteer = choice(volunteers)
	return volunteer

def handle_donation(donor, recipient):
	"""chooses inactive/undeclined volunteer and sends them invite to mission"""
	sms = SMS()
	# find a valid volunteer (i.e., not already busy or declined)
	volunteer = choose_volunteer()
	# globally-store the fact we've invited vol to deliver
	invitations[volunteer.mobile] = (donor, recipient)
	# issue the message
	sms.send_msg(volunteer.mobile,
		"A food pickup is ready for you at {} ({}). Text 'Yes' to accept this mission, or 'No' to decline.".format(
			donor.name, donor.location))

def cleanup(phone_number):
	"""Removes entries for volunteer from all global maps"""
	cleanup_list = [invitations, declined, deliveries]
	# clean up state
	for l in cleanup_list:
		try:
			del l[phone_number]
		except:
			print "cleanup is missing keys!"


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

@index.route('/about', methods=['GET'])
def about():
    return render_template("about.html", current_user=current_user)

@index.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", current_user=current_user)

# def debug(resp):
# 	resp.message("I hear you, {}, you said {}".format(
# 		request.form.get('From', ''), request.form.get('Body', '')))

@index.route('/respond', methods=['GET', 'POST'])
def respond():
	"""receives all incoming SMS messages"""
	try:
		resp = twiml.Response()
		sms = SMS()
		# grab the incoming volunteer phone number and the msg they sent
		from_number = request.form.get('From', '')
		body = request.form.get('Body', '')
		# find the volunteer entry by phone number
		volunteer = volunteer_map.get(from_number, None)

		# volunteer is at delivery phase, finishing!
		if 'in-delivery' in session:
			# send two messages to both
			feedback_url = "http://google.com"
			sms.send_msg(volunteer.mobile, "Thank you for your service! Please visit {} to rate your experience!".format(feedback_url))
			# sms.send_msg(recipient.mobile, )
			cleanup(volunteer.mobile)
		# volunteer is at picking up stage, time to deliver parcel
		elif 'claimed' in session:
			(donor, recipient) = deliveries[body] = invitations[from_number]
			resp.message("Please deliver the parcel to {}, and text 'done' when delivered.".format(recipient.location))
			session['in-delivery'] = True
		# volunteer is responding to initial invitation, so decide yes or no
		elif from_number in invitations:
			# if no, need to mark volunteer as declined and retry the invite
			if 'n' in body.lower():
				# remove from invitations
				invite = invitations.pop(from_number)
				declined[from_number] = True
				# re-invite next volunteer
				handle_donation(*invite)
			# otherwise they said yes
			else:
				# claim the pickup for the volunteer
				session['claimed'] = from_number
				# ...and msg them to text back when they pickup the parcel
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
