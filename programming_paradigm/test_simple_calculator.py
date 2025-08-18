import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(2,0), 2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,4), -1)

        self.assertEqual(self.calc.subtract(5,2), 3)

        self.assertEqual(self.calc.subtract(-2,-3), 1)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-2,-3),6)
        self.assertEqual(self.calc.multiply(2,-3), -6)

    def test_division(self):
        self.assertEqual(self.calc.divide(4,2), 2)

        self.assertEqual(self.calc.divide(4,0), None)
