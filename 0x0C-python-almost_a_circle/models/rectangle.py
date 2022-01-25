#!/usr/bin/python3
"""Module with base class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """This class is inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates Rectangle width 4 arguments:
        width, height, x, and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width"""
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height"""
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Retrieves x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x value"""
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Retrieves y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value"""
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        return self.width * self.height
