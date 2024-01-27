#!/usr/bin/python3
"""
This Module is For :
- <matrix_divided> Function

Author : Seif Mohamed
"""


def matrix_divided(matrix, div):

    """
    Description: This Function Adds Two intergers
    Arguments :
        - matrix : Input Matrix From User
        - div : Number To Divide The Matrix With
    Return : matrix / div if the Checks are Complete
    """
    # Check Div Condtions

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check Matrix Conditions

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    Rsize = len(matrix[0])

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if len(row) != Rsize:
            raise TypeError("Each row of the "
                            "matrix must have the same size")

        for e in row:
            if type(e) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(e / div, 2) for e in r] for r in matrix]
