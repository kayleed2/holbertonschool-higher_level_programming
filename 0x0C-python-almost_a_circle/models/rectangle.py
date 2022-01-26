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
        """Returns area"""
        return self.width * self.height

    def display(self):
        """Displays using #"""
        row = self.width * '#'
        for l in range(self.y):
            print()
        for i in range(self.height):
            for n in range(self.x):
                print(" ", end="")
            print(row)

    def __str__(self):
        """Representation when printed"""
        rec = 'Rectangle'
        l = f'[{rec}] {self.id} {self.x}/{self.y} - {self.width}/{self.height}'
        return l

    def update(self, *args, **kwargs):
        """Updates arguments"""
        count = 1
        if args is not None and len(args) != 0:
            for el in args:
                if count == 1:
                    self.id = el
                if count == 2:
                    self.width = el
                if count == 3:
                    self.height = el
                if count == 4:
                    self.x = el
                if count == 5:
                    self.y = el
                count += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
