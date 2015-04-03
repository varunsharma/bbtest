import unittest
from bbtest.fact import add


class TestAdd(unittest.TestCase):

    def test_add_fails(self):
        self.assertEqual(add(1,2), 5)


if __name__ == '__main__':
    unittest.main()
