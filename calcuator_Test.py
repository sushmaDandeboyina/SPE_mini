import unittest
import math
from calculator import squareRoot, powerFunction

class Cal_testing(unittest.TestCase):
    def test_positive_squareRoot(self):
        self.assertEqual(squareRoot(9),3)
        self.assertEqual(squareRoot(25),5)
        self.assertAlmostEqual(squareRoot(3),1.732, places=3)
        self.assertAlmostEqual(squareRoot(4.8),2.190, places=3)
        self.assertNotEqual(squareRoot(16),2)
    
    def test_zero_squareRoot(self):
        self.assertEqual(squareRoot(0),0)
        self.assertNotEqual(squareRoot(0),2)
    
    def test_negative_squareRoot(self):
        self.assertEqual(squareRoot(-6),"Square root cannot be computed for negative numbers")
        self.assertNotEqual(squareRoot(-9),3)

    def test_positive_powerFunction(self):
        self.assertEqual(powerFunction(3, 3), 27)  
        self.assertEqual(powerFunction(2, 5), 32)
        self.assertNotEqual(powerFunction(2, 5), 30)
    
    def test_zero_powerFunction(self):
        self.assertEqual(powerFunction(0, 5), 0) 
        self.assertEqual(powerFunction(0, 0), 1) 
        self.assertNotEqual(powerFunction(5, 0), 0)

    def test_negative_powerFunction(self):
        self.assertEqual(powerFunction(4, -1), 0.25) 
        self.assertEqual(powerFunction(-2,3), -8)
        self.assertNotAlmostEqual(powerFunction(-3,-2), -0.111,places = 3) 

    def test_positive_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertNotEqual(factorial(10), 362880)

    def test_zero_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_negative_factorial(self):
        self.assertEqual(factorial(-5), "Factorial cannot be computed for negative numbers")
        self.assertNotEqual(factorial(-3), 6)

if __name__ == "__main__": 
    unittest.main()


        