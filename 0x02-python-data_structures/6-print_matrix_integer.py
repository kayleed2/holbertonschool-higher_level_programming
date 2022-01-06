#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    for row in matrix:
        for ele in row:
            if ele is row[-1]:
                print("{:d}".format(ele))
            else:
                 print("{:d}".format(ele), end=' ')
       