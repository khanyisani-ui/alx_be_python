import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, 2), -7)
        self.assertEqual(self.calc.subtract(-7, -5), -2)
        
    def test_division(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(25, 5), 5)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        
    def test_multiplication(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(-7, -5), 35)
        
        
if __name__ == "__main__" :
    unittest.main()

# Remember to write additional test methods for subtract, multiply, and divide.