import unittest
import romans

class romansTest(unittest.TestCase):
	def test_cas1(self):
		self.assertEqual(romans.transformar(1),'I')
	def test_cas2(self):
		self.assertEqual(romans.transformar(2),'II')

unittest.main()