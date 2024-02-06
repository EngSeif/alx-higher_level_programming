#!/usr/bin/python3
"""
This Module Contains :-
    -    Student Class
"""


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        result = dict()
        if attrs is None:
            return self.__dict__
        else:
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
        return result   
