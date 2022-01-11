#!/usr/bin/python3
"""Class Square - Defines squares based on 1-sq"""


class Square:
    """Class Square - Defines squares based on 1-sq"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return ((self.__size) ** 2)
