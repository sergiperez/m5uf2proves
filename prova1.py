import unittest
import p2funciones2

class ATest(unittest.TestCase):
    def test_Acas1(self):
    #cas 1: camp buit
        self.assertEqual(p2funciones2.A("","b"), 0)
    def test_Acas2(self):
    #cas 2: lletra que no es troba al nom
        self.assertEqual(p2funciones2.A("eric","b"), 0)
    def test_Acas3(self):
    #cas 3: lletra que es troba al nom
        self.assertEqual(p2funciones2.A("eric","c"), 1)
        
unittest.main()
