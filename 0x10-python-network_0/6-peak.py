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
    if  len(list_of_integers) == 0:
        return None
    midpoint = len(list_of_integers) // 2
    half_1 = list_of_integers[:midpoint]
    half_2 = list_of_integers[midpoint:]
    if sum(half_1) > sum(half_2):
        if len(half_1) == 1:
            return half_1[0]
        return find_peak(half_1)
    else:
        if len(half_2) == 1:
            return half_2[0]
        return find_peak(half_2)