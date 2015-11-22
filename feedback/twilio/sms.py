#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twilio.rest import TwilioRestClient
import xml.etree.ElementTree as ET

from feedback.config import app_config

class SMS(object):

	account_phone = '+15672986849'

	def __init__(self):
		self.client = self.client_factory()

	def client_factory(self):
		return TwilioRestClient(app_config.TWILIO_AUTH, app_config.TWILIO_AUTH)

	def send_msg(self, dest, msg):
		self.client.messages.create(
			to="+1{}".format(dest), from_=self.account_phone, body=msg)

	def receive_msg(self, request):
		# TODO: find the sender and the msg
		# resp = ET.fromstring(data)
		# resp.findall('./Message/Body').pop().text
		# values.get('From') # incoming phone number
		# print request.values # FIXME/DEBUG
		return (request.form.get('From', ''), request.form.get('Body', ''))


if __name__ == '__main__':
	pass
