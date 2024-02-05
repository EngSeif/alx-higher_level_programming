#!/usr/bin/python3
"""
This Module Has:
-   MyList Class
"""


class MyList(list):
    """
    MyList Class
    Inheritance : List DataType
    """

    def print_sorted(self):
        print(sorted(self))
