#!/usr/bin/python3
"""
This Module is For :
- <print_square> Function

Author : Seif Mohamed
"""


def print_square(size):

    """
    Description: This Function Prints Square
    Arguments :
        - size : size of Square
    Return : None
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
