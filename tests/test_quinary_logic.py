import unittest
from quinary_logic import decimal_to_quinary, quinary_to_decimal

class TestOperations(unittest.TestCase):
    
    def test_decimal_to_quinary(self):
        self.assertEqual(decimal_to_quinary(10), 20)
        self.assertEqual(decimal_to_quinary(0), 0)
        self.assertEqual(decimal_to_quinary(4), 4)
        self.assertEqual(decimal_to_quinary(25), 100)

    def test_quinary_to_decimal(self):
        self.assertEqual(quinary_to_decimal(20), 10)
        self.assertEqual(quinary_to_decimal(0), 0)
        self.assertEqual(quinary_to_decimal(4), 4)
        self.assertEqual(quinary_to_decimal(100), 25)

if __name__ == '__main__':
    unittest.main()