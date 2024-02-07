#!/usr/bin/python3
"""
This Module Has:
-   MyInt Class
"""


class MyInt(int):
    """ My Custom Int Class """

    def __eq__(self, obj):
        return super().__ne__(obj)

    def __ne__(self, obj):
        return super().__eq__(obj)
