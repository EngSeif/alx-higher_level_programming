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
        self.x = x
        self.y = y

    def area(self):
        """ Return Area Of Rectangle """
        return self.width * self.height

    def display(self):
        """ Print Rectangle With # """
        for i in range(0, self.y):
            print()
        for h in range(0, self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        R_Dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return R_Dict

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, w):
        """ Width Setter """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, h):
        """ Height Setter """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """ X Getter """
        return self.__x

    @x.setter
    def x(self, xa):
        """ X Setter """
        if type(xa) is not int:
            raise TypeError("x must be an integer")
        if xa < 0:
            raise ValueError("x must be >= 0")
        self.__x = xa

    @property
    def y(self):
        """ Y Getter """
        return self.__y

    @y.setter
    def y(self, ya):
        """ Y Setter """
        if type(ya) is not int:
            raise TypeError("y must be an integer")
        if ya < 0:
            raise ValueError("y must be >= 0")
        self.__y = ya
