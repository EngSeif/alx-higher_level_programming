#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""

import json


class Base:
    """ The Base Of All Other Classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Base Constructor """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            Dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            Dummy = cls(1)
        Dummy.update(**dictionary)
        return Dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as Ofile:
                j_data = Ofile.read()
                dict_obj = cls.from_json_string(j_data)
                instances = [cls.create(**data) for data in dict_obj]
                return instances
        except FileNotFoundError:
            return []
