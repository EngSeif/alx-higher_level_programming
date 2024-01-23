#!/usr/bin/python3
""" This Module Defines Class: Square With Size
    And Validates If the Size Entered is Valid
"""


class Square:
    """ Class of Square That Intializes
    the Size of Square
    """
    __size = 0

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
