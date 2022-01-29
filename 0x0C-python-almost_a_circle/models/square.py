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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates arguments"""
        count = 1
        if args is not None and len(args) != 0:
            for el in args:
                if count == 1:
                    self.id = el
                if count == 2:
                    self.size = el
                if count == 3:
                    self.x = el
                if count == 4:
                    self.y = el
                count += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle"""
        the_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return the_dict
