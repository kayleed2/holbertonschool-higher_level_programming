#!/usr/bin/python3
"""Class Square - Defines squares based on 2-sq"""


class Square:
    """Class Square - Defines squares based on 2-sq"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0):
            self.__size = size

    def area(self):
        return self.__size ** 2
