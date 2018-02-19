#encoding: utf-8

import aprova
import unittest

class introTest(unittest.TestCase):
	def test_cas1(self):
		#cas 1: un negatiu
		self.assertEqual(aprova.aprova([1,5,7]),[5,5,7])
	def test_cas2(self):
		#cas 2: tots positius
		self.assertEqual(aprova.aprova([5,8,10]),[5,8,10])
	def test_cas3(self):
		#cas 3: tots negatius
		self.assertEqual(aprova.aprova([1,2,3]),[5,5,5])

unittest.main()
