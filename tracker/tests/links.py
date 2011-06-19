# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a  copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 444  Castro Street, Suite 900, Mountain View, California, 94041, USA.
# Date: 19/09/2010
# Author: Valder Gallo
# E-mail: valdergallo@gmail.com
# encoding: utf-8

from django.test import TestCase
from tracker.models import Browser, Domain, Ip, Log

class LinksTest(TestCase):

    def setUp(self):
        pass

    def test_domain(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
