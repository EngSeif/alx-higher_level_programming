#!/usr/bin/python3
"""
This Module Has:
-   BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry
    Inheritance : None
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle
    Inheritance : BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__width = width
