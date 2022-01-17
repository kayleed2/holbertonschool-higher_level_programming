#!/usr/bin/python3
""" Function that divides all elements of a matrix
python3 -c 'print(__import__("my_module").__doc__)'"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
    python3 -c 'print(__import__("my_module").__doc__)'
    matrix_divided - divides elements of matrix
    matrix: matrix to divide
    div: number divided by
    Return: new matrix
    """
    err = 'matrix must be a matrix (list of lists) of integers/floats'
    for row in matrix:
        for el in row:
            if isinstance(el, (int, float)) is False:
                raise TypeError(err)
    length = len(row)
    for row in matrix:
        if length != len(row):
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
