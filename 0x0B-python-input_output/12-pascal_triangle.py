#!/usr/bin/python3
"""
This Module Contains :-
    -    pascal_triangle(n)
"""


def pascal_triangle(n):
    """
    Description:
    -   returns a list of lists of integers representing
        the Pascal’s triangle of n
    Args:
    -   n : Number Of Lists

    Return :
        a list of lists
    """
    if n <= 0:
        return []
    result = []
    for i in range(0, n+1):
        if i == 0:
            result.append([1])
            continue
        if i == 1:
            result.append([1, 1])
            continue
        inner = []
        for j in range(0, i):
            if j == 0 or j == i - 1:
                inner.append(1)
                continue
            cal = result[i - 1][j - 1] + result[i - 1][j]
            inner.append(cal)
        result.append(inner)
    return result
