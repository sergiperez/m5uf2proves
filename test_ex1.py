#!/usr/bin/env python
# -*- coding: utf-8 -*-
import exercici1 as ex1
import unittest

class test_ex1(unittest.TestCase):
    def test_cas1(self):
        self.assertEqual(len(ex1.CrearLlista(2)),2)
    def test_cas2(self):
        self.assertEqual(len(ex1.CrearLlista(0)),0)

unittest.main()
