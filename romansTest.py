import unittest
import romans

class romansTest(unittest.TestCase):
	def test_cas1(self):
		self.assertEqual(romans.transformar(1),'I')

unittest.main()