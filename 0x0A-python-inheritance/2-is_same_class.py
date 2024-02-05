#!/usr/bin/python3
"""
This Module Has:
-   is_same_class(obj, a_class) Function
"""


def is_same_class(obj, a_class):
    """
    This Function :
        returns True if the object is exactly an instance of
        the specified class otherwise False.
    """
    return type(obj) is a_class
