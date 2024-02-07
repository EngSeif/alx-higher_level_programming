#!/usr/bin/python3
"""
This Module Has:
-   add_attribute(obj, attr, value)
"""


def add_attribute(obj, attr, value):
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
