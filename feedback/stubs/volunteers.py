##!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Donor = namedtuple('Donor', ('name', 'location', 'offering'))

Volunteer = namedtuple('Volunteer', ('name', 'mobile', 'location'))

Recipient = namedtuple('Recipient', ('handle', 'location', 'need_profile'))


if __name__ == '__main__':
	pass
