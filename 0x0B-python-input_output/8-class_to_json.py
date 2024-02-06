#!/usr/bin/python3
"""
This Module Contains :-
    -    class_to_json(obj)
"""

import json


def class_to_json(obj):
    """
    Description:
    -   returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

    Args:
    -   obj : Object TO Perform On

    Return :
        None
    """
    result = dict()
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
