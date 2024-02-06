#!/usr/bin/python3
"""
This Module Contains :-
    -    write_file(filename="", text="")
"""


def write_file(filename="", text=""):
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
    with open(filename, mode="w", encoding="utf-8") as rFile:
        return rFile.write(text)
