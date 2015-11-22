#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twilio.rest import TwilioRestClient
import xml.etree.ElementTree as ET


class SMS(object):

	account_phone = '+15672986849'
	account_sid = "AC0ff6bf2823297f5a1a037952031020f7"
	auth_token = "a78e9dc2b6f9ff8aad6440e6d1393e02"

	def __init__(self):
		self.client = self.client_factory()

	def client_factory(self):
		return TwilioRestClient(self.account_sid, self.auth_token)

	def send_msg(self, dest, msg):
		self.client.messages.create(to=dest, from_=self.account_phone, body=msg)

	def receive_msg(self, request):
		# TODO: find the sender and the msg
		# resp = ET.fromstring(data)
		# resp.findall('./Message/Body').pop().text
		# values.get('From') # incoming phone number
		# print request.values # FIXME/DEBUG
		return (request.form.get('From', ''), request.form.get('Body', ''))


if __name__ == '__main__':
	pass
