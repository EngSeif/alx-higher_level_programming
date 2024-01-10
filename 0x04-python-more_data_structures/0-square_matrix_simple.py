#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nMaxtrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return nMaxtrix
