#!/usr/bin/python3
""" This Module Is To Test Base Class"""


import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test Cases Class For Base Class """

    test_dir = 'test_files'

    def setUp(self):
        # Create a temporary directory for testing
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.rmdir(self.test_dir)

    def test_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_class(self):
        """ Test Rectangle class type """
        self.assertEqual(str(Base),
                         "<class 'models.base.Base'>")

    def test_class_inheritance(self):
        """ Test if Rectangle inherits from Base """
        self.assertTrue(issubclass(Base, Base))

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

    def test_toJson(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        json_dictionary = Base.to_json_string([r1.to_dictionary()])
        result = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(json.loads(json_dictionary), result)
        self.assertIsInstance(json_dictionary, str)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

        list_dictionaries = [{'id': 1, 'name': 'Alice'},
                             {'id': 2, 'name': 'Bob'}]
        expected_result = ('[{"id": 1, "name": "Alice"}, '
                           '{"id": 2, "name": "Bob"}]')
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         expected_result)

        list_dictionaries = [{'id': 1, 'info': {'name': 'Alice', 'age': 30}},
                             {'id': 2, 'info': {'name': 'Bob', 'age': 25}}]
        expected_result = '[{"id": 1, "info": {"name": "Alice", "age": 30}}, '\
                          '{"id": 2, "info": {"name": "Bob", "age": 25}}]'
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         expected_result)

    def test_save_to_file_empty_list(self):
        # Test when list_objs is an empty list
        filename = os.path.join(self.test_dir, 'Rectangle.json')
        Base.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_none(self):
        # Test when list_objs is None
        filename = os.path.join(self.test_dir, 'Rectangle.json')
        Base.save_to_file(None)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_single_object(self):
        # Test when list_objs contains a single object
        filename = os.path.join(self.test_dir, 'Rectangle.json')
        rectangle = Rectangle(1, 2)
        Base.save_to_file([rectangle])
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2}]')

    def test_save_to_file_multiple_objects(self):
        # Test when list_objs contains multiple objects
        rectangle_file = os.path.join(self.test_dir, 'Rectangle.json')
        square_file = os.path.join(self.test_dir, 'Square.json')
        rectangle = Rectangle(1, 2)
        square = Square(3)
        Base.save_to_file([rectangle, square])
        self.assertTrue(os.path.exists(rectangle_file))
        self.assertTrue(os.path.exists(square_file))
        with open(rectangle_file, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2}]')
        with open(square_file, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 2, "size": 3}]')


if __name__ == '__main__':
    unittest.main()
