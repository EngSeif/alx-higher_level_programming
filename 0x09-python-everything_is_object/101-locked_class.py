#!/usr/bin/python3
""" This Module Contains Locked Class """


class LockedClass:
    """ Class That Has No Attributes """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("{} object has no attribute {}"
                                 .format(LockedClass.__name__, name))
