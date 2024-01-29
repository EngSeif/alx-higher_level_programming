#!/usr/bin/python3
""" This Module Defines an Empty Class Rectangle """


class Rectangle:
    """ An Empty Class of Rectangle That does Nothing"""

    def __init__(self, width=0, height=0):
        """ Constructor Of Class Instance"""
        self.width = width
        self.height = height

    @property
    def width(self):

        """ Getter : Returns The Width Of Rectangle """
        return self.__width

    @width.setter
    def width(self, value):

        """ Setter : Sets The Width Of Rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ Getter : Returns The Height Of Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter : Sets The Height Of Rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
