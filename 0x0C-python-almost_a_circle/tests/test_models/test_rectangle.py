#!/usr/bin/python3
""" This Module Is To Test Rectnagle Class"""

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test Cases Class For Base Class """
    def test_Getters_Setters(self):
        """ 
        -   Test Getters And Setters
        """
        r1 = Rectangle(4, 5, 0, 2)
        r1.width = 6
        r1.height= 15
        r1.x = 7
        r1.y = 3
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 15)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 3)

    def test_InputInt(self):
        """ Test That Input Must Be int """
        r = Rectangle(4, 5, 0, 2)
        # Width Test
        self.assertRaises(TypeError, r.width, 5.1)
        self.assertRaises(TypeError, r.width, True)
        self.assertRaises(TypeError, r.width, [1, 2, 3])
        self.assertRaises(TypeError, r.width, {"Key" : 5})
        # Height Test
        self.assertRaises(TypeError, r.height, -5.1)
        self.assertRaises(TypeError, r.height, False)
        self.assertRaises(TypeError, r.height, [7, 5, 3, -8])
        self.assertRaises(TypeError, r.height, {0 : True})
        # x Test
        self.assertRaises(TypeError, r.x, -5.7)
        self.assertRaises(TypeError, r.x, False)
        self.assertRaises(TypeError, r.x, [7, -7, 3, -8])
        self.assertRaises(TypeError, r.x, {0 : (1, 2)})
        # y Test
        self.assertRaises(TypeError, r.x, 5.7)
        self.assertRaises(TypeError, r.x, True)
        self.assertRaises(TypeError, r.x, [7, -7, 8, -8])
        self.assertRaises(TypeError, r.x, {"HeHe" : (1, 2)})

    def test_InputValues(self):
        r = Rectangle(4, 5, 3, 2)
        
        with  self.assertRaises(ValueError):
            # Test Width And Height
            r.width = 0
            r.height = 0
            r.width = -9
            r.height = -18
            # Test X and Y
            r.x = -7
            r.y = -22
        self.x = 0
        self.y = 0
        self.assertEqual(self.x, 0)
        self.assertEqual(self.y, 0)


if __name__ == '__main__':
    unittest.main()