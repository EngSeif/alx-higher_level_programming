#!/usr/bin/python3
"""
This Module is For :
- <add_integer> Function

Author : Seif Mohamed
"""


def add_integer(a, b=98):
    """
    Description: This Function Adds Two intergers
    Arguments :
        - a : First Integer
        - b : Second Integer
    Return : a + b if the Checks are Complete
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
