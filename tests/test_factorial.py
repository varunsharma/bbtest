import unittest
#from __future__ import absolute_import
from bbtest.fact import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial_passes(self):
        self.assertEqual(factorial(5), 120)
        self.assertNotEqual(factorial(2), 120)

#    def test_factorial_fails(self):
#        self.assertEqual(factorial(5), 121)
#        self.assertEqual(factorial(2), 121)


if __name__ == '__main__':
    unittest.main()
