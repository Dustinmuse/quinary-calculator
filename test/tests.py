from advanced_operations import AdvancedOperations
import unittest

operator = AdvancedOperations()

class testOperations(unittest.TestCase):
    def testSquare(self):
        self.assertTrue(operator.sqaure(2), 4)

    def testSquareRoot(self):
        self.assertTrue(operator.square_root(25), 5)


if __name__ == '__main__':
    unittest.main()