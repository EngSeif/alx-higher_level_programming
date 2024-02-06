#!/usr/bin/python3
"""
This Module Contains :-
    -    to_json_string(my_obj)
"""

import json


def to_json_string(my_obj):
    """
    Description:
    -  returns the JSON representation of an object (string)

    Args:
    -   my_obj : Object To Convert Into JSON Representation

    Return :
        None
    """
    return json.dumps(my_obj)
