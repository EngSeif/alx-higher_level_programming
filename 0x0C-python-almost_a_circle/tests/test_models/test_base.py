#!/usr/bin/python3
""" This Module Is To Test Base Class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Cases Class For Base Class """
    def test_id(self):
        """ 
        -   Test Id With Different Values
        -   Id Is Assumed to Be Integer So
            We Dont Need To Test It
        """
        ob = Base()
        self.assertEqual(ob.id, 1)
        ob = Base()
        self.assertEqual(ob.id, 2)
        ob = Base(5)
        self.assertEqual(ob.id, 5)
        ob = Base(-3)
        self.assertEqual(ob.id, -3)
        ob = Base(5.4)
        self.assertEqual(ob.id, 5.4)
        ob = Base(-6.7)
        self.assertEqual(ob.id, -6.7)
        ob = Base(True)
        self.assertEqual(ob.id, True)
        ob = Base([1, 2, 3])
        self.assertEqual(ob.id, [1, 2, 3])
        ob = Base(None)
        self.assertEqual(ob.id, 3)
        ob = Base("Str")
        self.assertEqual(ob.id, "Str")
        ob = Base(0)
        self.assertEqual(ob.id, 0)

    def test_nbObj(self):
        """ Test If __nb__objects Is Private """
        ob = Base()
        with self.assertRaises(AttributeError):
            print(ob.__nb_objects)


if __name__ == '__main__':
    unittest.main()