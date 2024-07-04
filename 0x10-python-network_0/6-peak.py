#!/usr/bin/python3
"""
Module of find_peak Function
"""

def find_peak(list_of_integers):
    """
    Find Biggest Number
    """
    if len(list_of_integers) == 0:
        return None
    big = -9000
    for num in list_of_integers:
        if num > big:
            big = num
    return big