#!/usr/bin/python3
"""
This Module Contains :-
    -    save_to_json_file(my_obj, filename)
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Description:
    -  writes an Object to a text file, using a JSON representation

    Args:
    -   filename : Name Of The File (str)
    -   my_obj : Object To Convert Into JSON Representation

    Return :
        None
    """
    with open(filename, encoding="utf-8") as rFile:
        json.dump(my_obj, rFile)
