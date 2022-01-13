#!/usr/bin/python3
""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    err = 'matrix must be a matrix (list of lists) of integers/floats'
    for row in matrix:
        for el in row:
            if isinstance(el, (int, float)) is False:
                raise TypeError(err)
    for row in matrix:
        length = len(row)
        if length is not length:
            raise TypeError('Each row of the matrix must have the same size')
    if isinstance(div, (int, float)) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new = []
    for row in range(len(matrix)):
        new.append(list(map(lambda i: i / div, matrix[row])))
        new[row] = list(map(lambda r: round(r, 2), new[row]))
    return new