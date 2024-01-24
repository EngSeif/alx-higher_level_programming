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
    __postion = (0, 0)

    def __init__(self, size=0, postion=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(postion) is not tuple or len(postion) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(e, int) and e >= 0 for e in postion):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = postion

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

    @property
    def position(self):
        """ Returns The Postion of Square"""
        return self.__postion

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(e, int) and e >= 0 for e in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def my_print(self):
        """ Prints The Square"""
        if self.__size == 0:
            print()
        else:
            if self.__postion[1] > 0:
                for i in range(0, self.__postion[1]):
                    print()
            for i in range(0, self.__size):
                print(" " * self.__postion[0] + "#" * self.__size)

    def __str__(self):
        """ Print Human Readable Info"""
        Output = ""
        if self.__size == 0:
            Output = "\n"
        else:
            if self.__postion[1] > 0:
                Output += "\n" * self.__postion[1]
            for i in range(0, self.__size):
                Output += " " * self.__postion[0] + "#" * self.__size + "\n"
        return Output.rstrip()
