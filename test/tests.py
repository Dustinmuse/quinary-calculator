from advanced_operations import square, square_root
import unittest

operator_advanced = AdvancedOperations()

class testOperations(unittest.TestCase):
    def testSquare(self):
        self.assertTrue(operator_advanced.sqaure(2), 4)

    def testSquareRoot(self):
        self.assertTrue(operator_advanced.square_root(25), 5)


if __name__ == '__main__':
    unittest.main()