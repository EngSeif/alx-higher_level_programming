#!/usr/bin/python3
"""
This Module is For :
- <say_my_name> Function

Author : Seif Mohamed
"""


def say_my_name(first_name, last_name=""):

    """
    Description: This Function Prints the Name Of A Person
    Arguments :
        - first_name : First Name Of Person
        - last_name : Last Name Of Person
    Return : None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
