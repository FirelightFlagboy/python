import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../Class'))

from Maps import Maps
import unittest
import re

class MapsTest(unittest.TestCase):

	def setUp(self):
		self.map = Maps("test")

	def testChoice(self):
		choiceSimple = "1"
		choiceBig = "124654987532156489"
		choiceNegSimple = "-1"
		choiceNegBig = "-123548796"
		self.assertNotEqual(re.search(self.map.ex_choice, choiceSimple), None)
		self.assertNotEqual(re.search(self.map.ex_choice, choiceBig), None)
		self.assertEqual(re.search(self.map.ex_choice, choiceNegSimple), None)
		self.assertEqual(re.search(self.map.ex_choice, choiceNegBig), None)
