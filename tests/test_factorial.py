import unittest
#from __future__ import absolute_import
from bbtest.fact import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertNotEqual(factorial(2), 120)



if __name__ == '__main__':
    unittest.main()
