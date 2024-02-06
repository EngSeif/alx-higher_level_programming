#!/usr/bin/python3
"""
This Module Contains :-
    -    load_from_json_file(filename)
"""

import json


def load_from_json_file(filename):
    """
    Description:
    -  creates an Object from a “JSON file”

    Args:
    -   filename : Name Of The File (str)

    Return :
        None
    """
    with open(filename, mode="w", encoding="utf-8") as rFile:
        return json.load(rFile)
