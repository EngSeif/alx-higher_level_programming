#!/usr/bin/python3
""" This Module Defines Class: Square With Size
    - Validates If the Size Entered is Valid
    - Has Also A Method To Return the Area
    - Has A Setter and Getter To Change Size
"""


class Square:
    """ Class of Square That Contains
    - Parametrized Constructor
    - Area Function : Returns Square Area
    - Setters and Getters for Size
    """
    __size = 0

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ ReTurns The Area Of Square"""
        return self.__size**2

    @property
    def size(self):
        """ Returns Size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets The Size of Square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints The Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
