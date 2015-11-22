##!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Donor = namedtuple('Donor', ('name', 'location', 'offering'))

Volunteer = namedtuple('Volunteer', ('name', 'mobile', 'location'))

Recipient = namedtuple('Recipient', ('handle', 'location', 'need_profile'))

donors = (
	('Refectory', '', 'goat cheese, foie gras, porque, gabagool'),
	('Joe\'s Crab Shack', '', 'haddock, cod'),
	('Krogers', '', 'Milk, Bread, Eggs, Vegetables'),
	('Tim Hortons', '', 'coffee, donuts, bagels, bread'),
	('CVS', '', 'sandwiches, robitussin, quaaludes')
)

volunteers = (
	('Herman', '4435107985', ''),
	('Scott', '4192831501', ''),
	('Sam', '', ''),
	('James', '', '')
)

recipients = (
	('Addams Family', '', 'haddock, cod'),
	('The Sopranos', '', 'foie gras, porque, gabagool'),
	('The Simpsons', '', 'donuts'),
	('The Cosby\'s', '', 'Milk, Eggs, quaaludes')
)

def get_volunteers():
	return [Volunteer(v) for v in volunteers]

def get_donor():
	return [Donor(d) for d in donors]

def get_recipients():
	return [Recipients(r) for r in recipients]


if __name__ == '__main__':
	pass
