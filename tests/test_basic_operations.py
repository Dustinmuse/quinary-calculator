import unittest
from basic_operations import add, subtract, multiply, divide

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add("2", "2"), "4")

    def test_substract(self):
        self.assertEqual(subtract("4", "3"), "1")
    
    def test_multiply(self):
        self.assertEqual(multiply("3", "2"), "11")

    def test_divide(self):
        self.assertEqual(divide("4", "2"), "2")

    def test_divide_by_zero(self):
        self.assertEqual(divide("4", "0"), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()