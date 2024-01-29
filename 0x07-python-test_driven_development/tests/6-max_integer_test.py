#!/usr/bin/python3
"""
This Module is For :
- Testing < max_integer function>

Author : Seif Mohamed
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):

    """ Test Cases For max_integers"""
    def test_Empty(self):
        self.assertEqual(max_integer(), None)

    def test_cases(self):
        self.assertEqual(max_integer([1, 5, 4, 10, -8]), 10)
        self.assertEqual(max_integer([1, 5, 4, 10, 8]), 10)
        self.assertEqual(max_integer([-1, -5, -4, -10, -8]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([8, 8, 8]), 8)
        self.assertEqual(max_integer([5136, 52361, 105213, -853]), 105213)


if __name__ == "__main__":
    unittest.main()
