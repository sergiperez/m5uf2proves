#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import Exercici1
class calculadoraTest(unittest.TestCase):
	def test_provaSumar(self):
		self.assertEqual(Exercici1.sumar(2,2),4)
	def test_provaRestar(self):
		self.assertEqual(Exercici1.restar(3,2),1)
	def test_multiplicar(self):
		self.assertEqual(Exercici1.multiplicar(4,4),16)
	def test_dividir(self):
		self.assertEqual(Exercici1.dividir(6,2),(3, True))
unittest.main()
