#!/usr/bin/python3
"""
This Module Contains :-
    -    read_file(filename="") Function
"""


def read_file(filename=""):
    """
    Description:
    -   Reads Content Of File And Print It

    Args:
    -   filename = Name Of The File (str)

    Return :
        None
    """
    with open(filename, encoding="utf-8") as rFile:
        print(rFile.read(), end="")
