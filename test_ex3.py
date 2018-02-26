#!/usr/bin/env python
# -*- coding: utf-8 -*-
import exercici3 as ex3
import unittest

class test_ex3(unittest.TestCase):
    def test_cas1(self):
        self.assertEqual(ex3.desencripta_text(['GnkZ']),['Hola'])
    def test_cas2(self):
        self.assertEqual(ex3.desencripta_text([]),[])
    def test_cas3(self):
        self.assertEqual(ex3.desencripta_text(['$']),[])

unittest.main()
