import unittest
from bbtest.add import add


class TestAdd(unittest.TestCase):

    def test_add_fails(self):
        self.assertEqual(add(1,2), 5)

    def test_add_passes(self):
        self.assertEqual(add(1,2), 3)


if __name__ == '__main__':
    unittest.main()
