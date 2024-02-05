#!/usr/bin/python3
"""
This Module Has:
-   BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator(size)
        self.__size = size

    def area(self):
        return self.__size ** 2
