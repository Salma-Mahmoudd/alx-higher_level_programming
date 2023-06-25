#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    M = []
    for i in matrix:
        M.append(list(map(lambda x: x ** 2, i)))
    return M
