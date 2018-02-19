#!/usr/bin/env python
# -*- coding: utf-8 -*-
import exercicici3
import unittest

class exercicici3test(unittest.TestCase):
	def test_case1(self):
		#cas 1: llista amb un element negatiu [34]
		self.assertEqual(exercicici3.t([34]),[34])
	def test_case2(self):
		#cas2: llista amb més d'un element tot positiu [6,98,7]
		self.assertEqual(exercicici3.t([6,98,7]),[6,98,7])
	def test_case3(self):
		#cas3: llista amb més elements amb negatius [3,2,1]
		self.assertEqual(exercicici3.t([3,2,1]),[5,5,5])		
		
unittest.main()
