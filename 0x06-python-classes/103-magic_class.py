#!/usr/bin/python3
""" This Module Includes A MagicClass Object """
import math


class MagicClass:
    def __init__(self, radius):
        """ Constructor Of Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Return Area Of Circle """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Return Radius Of Circle """
        return 2 * math.pi * self.__radius
