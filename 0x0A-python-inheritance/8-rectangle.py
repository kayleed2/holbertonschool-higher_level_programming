#!/usr/bin/python3
"""This module contains  a class Rectangle that inherits
class BaseGeometry (based on 7-base_geometry.py):
python3 -c 'print(__import__("my_module").__doc__)'"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is based on BaseGeometry from
    the module 7-base_geometry.py:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def __init__(self, width, height):
        """This method instantiates with width and height:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
