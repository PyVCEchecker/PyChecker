# -*- coding: utf-8 -*-
import bottle, unittest

class TestRoutes(unittest.TestCase):

	def setUp(self):
		# mock bottle.run
		self.orig_run = bottle.run
		bottle.run = self.fake_run
		self.run_calls = []

	def fake_run(self, *a, **ka):
		self.run_calls.append((a, ka))

	def tearDown(self):
		bottle.run = self.orig_run

