#!/usr/bin/python3
"""
This Module Has:
-   inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    This Function :
        returns True if the object is an instance of
        a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """
    return issubclass(obj, a_class)
