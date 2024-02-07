#!/usr/bin/python3
"""
This Module Contains :-
    -    append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Description:
    -   inserts a line of text to a file,
        after each line containing a specific string
    Args:
    -   filename : Name Of The File
    -   search_string : String To Search For
    -   New_String : String To Put After Search String

    Return :
        None
    """
    with open(filename, encoding="utf-8") as InFile:
        lines = InFile.readlines()

    with open(filename, mode="w", encoding="utf-8") as OutFile:
        for line in lines:
            OutFile.write(line)
            if search_string in line:
                OutFile.write(new_string)
