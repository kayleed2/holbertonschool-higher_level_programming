#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle based on 2-rectangle.py """


class Rectangle:
    """Write a class Rectangle that defines
    a rectangle based on 2-rectangle.py"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            self.perimeter = 0
        else:
            self.perimeter = (self.__height * 2) + (self.__width * 2)
        return self.perimeter

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        height = self.__height
        for i in range(self.__height):
            for self.__height in range(self.__width):
                print("#", end="")
            if i == height - 1:
                continue
            else:
                print()
        return str()

    """def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'"""
