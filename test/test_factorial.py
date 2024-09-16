import unittest
from app import factorial

if __name__ == '__main__':
    unittest.main()

class TestFactorial(unittest.TestCase):

    # test for 0
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
    
    # test for 1
    def test_one(self):
        self.assertEqual(factorial(1), 1)
    
    # test a small number
    def test_five(self):
        self.assertEqual(factorial(5), 120)

    # test a big number
    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

if __name__ == '__main__':
    unittest.main()