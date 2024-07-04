#!/usr/bin/python3
"""
Module of find_peak Function
"""

def getBigger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def find_peak(list_of_integers):
    """
    Find Biggest Number
    """
    big = 0
    size = len(list_of_integers) - 1
    if  len(list_of_integers) == 0:
        return None
    half = (size // 2) + 1
    for i in range(0, half):
        if i == 0:
            big = getBigger(list_of_integers[i], list_of_integers[size-i])
        else:
            if big < getBigger(list_of_integers[i], list_of_integers[size-i]):
                big = getBigger(list_of_integers[i], list_of_integers[size-i])
    return big