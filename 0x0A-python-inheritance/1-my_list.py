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
        """ Print Sorted List """
        S_list = sorted(self)
        print(S_list)
