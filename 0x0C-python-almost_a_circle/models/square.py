#!/usr/bin/python3
"""This module contains class Square which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates with arguments size, x, y, and id"""
        width = size
        height = size
        self.size = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """Overwrites super str with different string"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
