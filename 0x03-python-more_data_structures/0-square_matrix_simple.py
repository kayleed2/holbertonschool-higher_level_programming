#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in range(len(matrix)):
        newmatrix.append(list(map(lambda i: i**2, matrix[row])))
    return newmatrix
