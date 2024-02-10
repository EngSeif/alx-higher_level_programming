#!/usr/bin/python3
"""
This Module Contains :
    - Rectangle Class That Inherits <--- Base
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Class Constructor """
        super().__init__(id)
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, w):
        """ Width Setter """
        self.__width = w

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, h):
        """ Height Setter """
        self.__height = h

    @property
    def x(self):
        """ X Getter """
        return self.__x

    @x.setter
    def height(self, xa):
        """ X Setter """
        self.__x = xa

    @property
    def y(self):
        """ Y Getter """
        return self.__y

    @y.setter
    def y(self, ya):
        """ Y Setter """
        self.__y = ya
