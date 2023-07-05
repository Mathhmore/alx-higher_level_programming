#!/usr/bin/python3
"""
module: 2-matrix_devided.py
contains a method that devide all elements of a matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    method that devides elements of matrix by div
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])
    for i in matrix:
        l = []
        if not isinstance(i, list):
            raise TypeError(msg)
        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(msg)
            l.append(round(float(j) / float(div), 2))
        new_matrix.append(l)
    return new_matrix
