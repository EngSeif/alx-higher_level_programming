#!/usr/bin/python3
""" This Module Defines an Empty Class Rectangle """


class Rectangle:
    """ An Empty Class of Rectangle That does Nothing"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor Of Class Instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Returns The Area Of Rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns The Perimeter Of Rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Prints Rectangle With # on Console"""
        result = ""
        if self.width == 0 or self.height == 0:
            return result
        else:
            for i in range(0, self.height):
                result += str(self.print_symbol) * self.width + "\n"
        return result.strip()

    def __repr__(self):
        """ A String Representation Of The Rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Destructor Of Class Instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
