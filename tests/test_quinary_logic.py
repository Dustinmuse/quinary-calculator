import unittest
from quinary_logic import QuinaryCalculator

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc = QuinaryCalculator()

    def test_decimal_to_quinary(self):
        self.assertEqual(self.calc.decimal_to_quinary(10), 20)
        self.assertEqual(self.calc.decimal_to_quinary(0), 0)
        self.assertEqual(self.calc.decimal_to_quinary(4), 4)
        self.assertEqual(self.calc.decimal_to_quinary(25), 100)

    def test_quinary_to_decimal(self):
        self.assertEqual(self.calc.quinary_to_decimal(20), 10)
        self.assertEqual(self.calc.quinary_to_decimal(0), 0)
        self.assertEqual(self.calc.quinary_to_decimal(4), 4)
        self.assertEqual(self.calc.quinary_to_decimal(100), 25)

if __name__ == '__main__':
    unittest.main()