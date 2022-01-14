#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle """


class Rectangle:
    """Write a class Rectangle that defines a rectangle """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width msut be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height msut be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
