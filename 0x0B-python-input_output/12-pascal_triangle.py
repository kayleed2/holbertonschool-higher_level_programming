#!/usr/bin/python3
"""Contains function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    list = [1]
    for el in range(n):
        print(list)
        newlist = []
        newlist.append(list[0])
        for i in range(len(list) - 1):
            newlist.append(list[i] + list[i + 1])
        newlist.append(list[-1])
        list = newlist
