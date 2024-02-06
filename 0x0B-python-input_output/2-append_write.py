#!/usr/bin/python3
"""
This Module Contains :-
    -    append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Description:
    -   Write Text To File And
        Returns Num Of Chars In Text

    Args:
    -   filename : Name Of The File (str)
    -   text : Text To Be Added In File

    Return :
        None
    """
    with open(filename, mode="a", encoding="utf-8") as rFile:
        return rFile.write(text)
