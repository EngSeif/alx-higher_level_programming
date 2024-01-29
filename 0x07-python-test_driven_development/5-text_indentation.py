#!/usr/bin/python3
"""
This Module is For :
- <text_indentation> Function

Author : Seif Mohamed
"""


def text_indentation(text):

    """
    Description:    prints a text with 2 new lines after
                    each of these characters: . ? and :
    Arguments :
        - Text : Text To perform Function On
    Return : None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    delimiters = ".?:"
    current = ""
    for Element in text:
        if Element in delimiters:
            print((current + Element).strip())
            print("\n", end="")
            current = ""
        else:
            current += Element
    print(current.strip(), end="")
