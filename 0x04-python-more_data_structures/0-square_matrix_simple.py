#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k = 0
    m = 0
    col = len(matrix[0])
    row = len(matrix)
    new_matrix = [[0 for _ in range(col)] for _ in range(row)]
    for i in matrix:
        for j in i:
            new_matrix[k][m] = j * j
            m += 1
        k += 1
        m = 0
    return new_matrix
