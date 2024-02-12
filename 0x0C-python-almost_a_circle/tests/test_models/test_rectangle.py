#!/usr/bin/python3
""" This Module Is To Test Rectnagle Class"""

from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test Cases Class For Rectangle Class """

    def setUp(self):
        # Set up the test fixture
        r = Rectangle(4, 5, 0, 2)

    def test_Getters_Setters(self):
        """
        -   Test Getters And Setters
        """
        r = Rectangle(4, 5, 0, 2)
        r.width = 6
        r.height = 15
        r.x = 7
        r.y = 3
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 3)

    def test_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)

    def test_class(self):
        """ Test Rectangle class type """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_class_inheritance(self):
        """ Test if Rectangle inherits from Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_arg_passed(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(20)
            Rectangle()

    def test_InputInt(self):
        """ Test That Input Must Be int """
        r = Rectangle(4, 5, 0, 2)
        # Width Test
        self.assertRaises(TypeError, r.width, 5.1)
        self.assertRaises(TypeError, r.width, True)
        self.assertRaises(TypeError, r.width, [1, 2, 3])
        self.assertRaises(TypeError, r.width, {"Key": 5})
        # Height Test
        self.assertRaises(TypeError, r.height, -5.1)
        self.assertRaises(TypeError, r.height, False)
        self.assertRaises(TypeError, r.height, [7, 5, 3, -8])
        self.assertRaises(TypeError, r.height, {0: True})
        # x Test
        self.assertRaises(TypeError, r.x, -5.7)
        self.assertRaises(TypeError, r.x, False)
        self.assertRaises(TypeError, r.x, [7, -7, 3, -8])
        self.assertRaises(TypeError, r.x, {0: (1, 2)})
        # y Test
        self.assertRaises(TypeError, r.x, 5.7)
        self.assertRaises(TypeError, r.x, True)
        self.assertRaises(TypeError, r.x, [7, -7, 8, -8])
        self.assertRaises(TypeError, r.x, {"HeHe": (1, 2)})

    def test_InputValues(self):
        r = Rectangle(4, 5, 3, 2)
        with self.assertRaises(ValueError):
            # Test Width And Height
            r.width = 0
            r.height = 0
            r.width = -9
            r.height = -18
            # Test X and Y
            r.x = -7
            r.y = -22
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_Area(self):
        r = Rectangle(4, 5, 0, 2)
        self.assertEqual(r.area(), 4 * 5)
        r = Rectangle(14, 6, 0, 2)
        self.assertEqual(r.area(), 14 * 6)
        r = Rectangle(58544, 57156, 0, 2)
        self.assertEqual(r.area(), 58544 * 57156)
        r = Rectangle(5, 6, 0, 2)
        r.width = 6
        self.assertEqual(r.area(), 6 * 6)
        r.height = 1
        self.assertEqual(r.area(), 6 * 1)

    def test_display(self):

        # Default Test

        r = Rectangle(3, 2)
        result = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

        r = Rectangle(3, 2, 1, 1)
        result = "\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

        # Change Width And Height With Setter

        r = Rectangle(3, 2)
        r.width = 4
        result = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)
        r = Rectangle(3, 2)

        r.height = 4
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

        # Change x and y with setter

        r = Rectangle(3, 2)
        r.x = 1
        r.y = 2
        result = "\n\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

        r = Rectangle(3, 2)
        r.x = 3
        r.y = 4
        result = "\n\n\n\n   ###\n   ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):

        # Default Test

        r = Rectangle(3, 2, 0, 0, 50)
        self.assertEqual(r.__str__(), "[Rectangle] (50) 0/0 - 3/2")

        # With X and Y

        r = Rectangle(3, 2, 4, 2, 50)
        self.assertEqual(r.__str__(), "[Rectangle] (50) 4/2 - 3/2")

        #  With Id

        r = Rectangle(5, 7, 4, 2, 198)
        self.assertEqual(r.__str__(), "[Rectangle] (198) 4/2 - 5/7")

        # Change With Setter And Getter Then Print

        r = Rectangle(5, 7, 4, 2, 198)
        r.width = 10
        r.height = 15
        r.id = 6
        r.x = 7
        r.y = 6
        self.assertEqual(r.__str__(), "[Rectangle] (6) 7/6 - 10/15")

    def test_Update(self):

        # Test Empty
        r = Rectangle(10, 10, 10, 10, 30)
        r.update()
        self.assertEqual(r.id, 30)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        # Test 1 Args

        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        # Test 2 Args

        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        # Test 3 Args

        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        # Test 4 Args

        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)

        # Test 5 Args

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        # Testing Kwargs

        r = Rectangle(10, 10, 10, 10, 700)

        r.update(height=1)
        self.assertEqual(r.id, 700)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(width=1, x=2)
        self.assertEqual(r.id, 700)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 10)

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

        # Test Args And Kwargs At Same Time

        r = Rectangle(10, 10, 10, 10, 700)

        r.update(5, height=1)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)


if __name__ == '__main__':
    unittest.main()
