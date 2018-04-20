import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../Class'))
from Class.Carte import Carte

class CarteTest(unittest.TestCase):

	"""
	Test la class Carte de Carte.py
	"""
	def setUp(self):
		self.test = {
			"zeroNl" : "OOOOOO",
			"sixNl" : "\n\n\n\n\n",
			"fullmap" :
				"OOOOOOOO\n"
				"O     UO\n"
				"OOOOOOOO"
		}

		self.carte = {}
		for key, val in self.test.items():
			self.carte[key] = Carte(key, val)

	def testConvStrDic(self):
		"""
		Verifier si la conversion de la chaine vers un dic et bien faite
		"""
		zeroNl = {
			(1, 1) : "O",
			(1, 2) : "O",
			(1, 3) : "O",
			(1, 4) : "O",
			(1, 5) : "O",
			(1, 6) : "O"
		}
		sixNl = {}
		fullmap = {
			(1, 1) : "O", (2, 1) : "O", (3, 1) : "O",
			(1, 2) : "O", (2, 2) : " ", (3, 2) : "O",
			(1, 3) : "O", (2, 3) : " ", (3, 3) : "O",
			(1, 4) : "O", (2, 4) : " ", (3, 4) : "O",
			(1, 5) : "O", (2, 5) : " ", (3, 5) : "O",
			(1, 6) : "O", (2, 6) : " ", (3, 6) : "O",
			(1, 7) : "O", (2, 7) : "U", (3, 7) : "O",
			(1, 8) : "O", (2, 8) : "O", (3, 8) : "O",
		}
		self.assertEqual(self.carte["zeroNl"].labyrinthe, zeroNl)
		self.assertEqual(self.carte["sixNl"].labyrinthe, sixNl)
		self.assertEqual(self.carte["fullmap"].labyrinthe, fullmap)

	def test__str__(self):
		"""
		Test la methode __str__
		"""
		for key, val in self.test.items():
			so = "test : " + val
			sv = "test : " + self.carte[key].__str__()
			self.assertEqual(sv, so)

	def test__repr__(self):
		"""
		Test la methode __repr__
		"""
		for key, val in self.carte.items():
			so = "<Carte " + key + ">"
			self.assertEqual(so, val.__repr__())
