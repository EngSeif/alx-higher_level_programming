#!/usr/bin/python3
"""
This Module Contains :
    - Square Class That Inherits <--- Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square Class Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, s):
        """ Size Setter """
        if type(s) is not int:
            raise TypeError("width must be an integer")
        if s <= 0:
            raise ValueError("width must be > 0")
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
