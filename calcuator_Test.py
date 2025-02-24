import unittest
import math
from calculator import squareRoot

class Cal_testing(unittest.TestCase):
    def test_positive_squareRoot(self):
        self.assertEqual(squareRoot(9),3)
        self.assertEqual(squareRoot(25),5)
        self.assertAlmostEqual(squareRoot(3),1.732, places=3)
        self.assertNotEqual(squareRoot(16),2)
    
    def test_zero_squareRoot(self):
        self.assertEqual(squareRoot(0),0)
        self.assertNotEqual(squareRoot(0),2)
    
    def test_negative_squareRoot(self):
        self.assertEqual(squareRoot(-6),"Square root cannot be computed for negative numbers")
        self.assertNotEqual(squareRoot(-9),3)

if __name__ == "__main__": 
    unittest.main()


        