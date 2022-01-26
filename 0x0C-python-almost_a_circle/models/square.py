#!/usr/bin/python3
"""This module contains class Square which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates with arguments size, x, y, and id"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overwrites super str with different string"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Returns size of square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets Square size"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
