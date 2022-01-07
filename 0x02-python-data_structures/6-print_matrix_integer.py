#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for ele in row:
            if ele is row[-1]:
                print("{}".format(ele), end="")
            else:
                 print("{:d}".format(ele), end=" ")
        print()
       