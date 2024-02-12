#!/usr/bin/python3
""" This Module Is To Test Rectnagle Class"""

from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test Cases Class For Square Class """

    def setUp(self):
        # Set up the test fixture
        s = Square(4, 5, 0, 2)

    def test_Getters_Setters(self):
        """
        -   Test Getters And Setters
        """
        s = Square(4, 5, 0, 2)
        s.x = 7
        s.y = 3
        s.size = 3
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 3)

    def test_docstring(self):
        self.assertIsNotNone(Square.__doc__)

    def test_class(self):
        """ Test Rectangle class type """
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_class_inheritance(self):
        """ Test if Rectangle inherits from Base """
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_arg_passed(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_InputInt(self):
        """ Test That Input Must Be int """
        s = Square(4, 5, 0, 2)
        # Size Test
        self.assertRaises(TypeError, s.size, 5.1)
        self.assertRaises(TypeError, s.size, True)
        self.assertRaises(TypeError, s.size, [1, 2, 3])
        self.assertRaises(TypeError, s.size, {"Key": 5})
        # x Test
        self.assertRaises(TypeError, s.x, -5.7)
        self.assertRaises(TypeError, s.x, False)
        self.assertRaises(TypeError, s.x, [7, -7, 3, -8])
        self.assertRaises(TypeError, s.x, {0: (1, 2)})
        # y Test
        self.assertRaises(TypeError, s.x, 5.7)
        self.assertRaises(TypeError, s.x, True)
        self.assertRaises(TypeError, s.x, [7, -7, 8, -8])
        self.assertRaises(TypeError, s.x, {"HeHe": (1, 2)})

    def test_InputValues(self):
        s = Square(4, 5, 0, 2)
        with self.assertRaises(ValueError):
            # Test Width And Height
            s.size = 0
            s.size = -9
            # Test X and Y
            s.x = -7
            s.y = -22
        s.x = 0
        s.y = 0
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_Area(self):
        s = Square(4, 5, 0, 2)
        self.assertEqual(s.area(), 4 ** 2)
        s = Square(14, 6, 0, 2)
        self.assertEqual(s.area(), 14 ** 2)
        s = Square(58544, 57156, 0, 2)
        self.assertEqual(s.area(), 58544 ** 2)
        s = Square(5, 6, 0, 2)
        s.size = 6
        self.assertEqual(s.area(), 6 ** 2)

    def test_display(self):

        # Default Test

        s = Square(3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

        s = Square(3, 2, 1, 1)
        result = "\n  ###\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

        # Change Width And Height With Setter

        s = Square(3)
        s.size = 4
        result = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

        # Change x and y with setter

        s = Square(4)
        s.x = 1
        s.y = 2
        result = "\n\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

        s = Square(2)
        s.x = 3
        s.y = 4
        result = "\n\n\n\n   ##\n   ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):

        # Default Test

        s = Square(3)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 0/0 - 3")

        s = Square(3, 0, 0, 50)
        self.assertEqual(s.__str__(), "[Square] (50) 0/0 - 3")

        # With X and Y

        s = Square(3, 4, 2, 50)
        self.assertEqual(s.__str__(), "[Square] (50) 4/2 - 3")

        #  With Id

        s = Square(5, 4, 2, 198)
        self.assertEqual(s.__str__(), "[Square] (198) 4/2 - 5")

        # Change With Setter And Getter Then Print

        s = Square(5, 4, 2, 198)
        s.size = 10
        s.id = 6
        s.x = 7
        s.y = 6
        self.assertEqual(s.__str__(), "[Square] (6) 7/6 - 10")

    def test_Update(self):

        # Test Empty
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

        # Test 1 Args

        s.update(89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

        # Test 2 Args

        s.update(89, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

        # Test 3 Args

        s.update(89, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 10)

        # Test 4 Args

        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        # Testing Kwargs

        s = Square(10, 10, 10, 10)

        s.update(size=1)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

        s.update(size=1, x=2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 10)

        s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)

        # Test Args And Kwargs At Same Time

        s = Square(5, 7, 8, 10)

        s.update(5, height=1)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)


if __name__ == '__main__':
    unittest.main()
