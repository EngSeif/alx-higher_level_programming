#!/usr/bin/python3
"""
This Module Contains :-
    -    from_json_string(my_str)
"""

import json


def from_json_string(my_str):
    """
    Description:
    -  returns the JSON representation of an object (string)

    Args:
    -   my_obj : Object To Convert To Py Representation

    Return :
        None
    """
    return json.loads(my_str)
