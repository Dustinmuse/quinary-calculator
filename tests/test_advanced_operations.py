import unittest
from advanced_operations import square, square_root

class TestOperations(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2), 4)

    def test_square_root(self):
        self.assertEqual(square_root(100), 10)

if __name__ == '__main__':
    unittest.main()