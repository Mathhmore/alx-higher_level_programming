#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k = 0
    l = 0
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in matrix:
        for j in i:
            new_matrix[k][l] = j * j
            l += 1
        k += 1
        l = 0
    return new_matrix
