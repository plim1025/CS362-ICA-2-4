import unittest
from calculator import addition, subtraction, multiplication, division

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(3, 3), 6)

    def test_additionFloat(self):
        self.assertAlmostEqual(addition(3.5, 4.24), 7.74)
    
    def test_additionNegative(self):
        self.assertAlmostEqual(addition(3.5, -3.5), 0)

    def test_invalidAddition(self):
        self.assertEqual(addition("bad input", 4), None)

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 2), 1)

    def test_subtractionNegative(self):
        self.assertEqual(subtraction(3, -2), 5)

    def test_subtractionFloat(self):
        self.assertAlmostEqual(subtraction(3, -0.5), 3.5)

    def test_invalidSubtraction(self):
        self.assertEqual(subtraction(5, "bad input"), None)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 2), 6)

    def test_multiplicationNegative(self):
        self.assertEqual(multiplication(3, -2), -6)

    def test_multiplicationFloat(self):
        self.assertAlmostEqual(multiplication(3, -0.5), -1.5)

    def test_invalidMultiplication(self):
        self.assertEqual(multiplication(5, "bad input"), None)

    def test_division(self):
        self.assertEqual(division(3, 1), 3)

    def test_divisionNegative(self):
        self.assertEqual(division(3, -1), -3)

    def test_divisionFloat(self):
        self.assertAlmostEqual(division(3, -2), -1.5)

    def test_invalidDivision(self):
        self.assertEqual(division(5, "bad input"), None)

    def test_divideByZeroDivision(self):
        self.assertEqual(division(5, 0), None)

if __name__ == "__main__":
    unittest.main()

