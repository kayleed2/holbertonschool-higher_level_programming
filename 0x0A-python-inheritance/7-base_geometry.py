#!/usr/bin/python3
"""This module contains  a class BaseGeometry
(based on 6-base_geometry.py:
python3 -c 'print(__import__("my_module").__doc__)'"""


class BaseGeometry():
    """This class is based on 6-base_geometry.py:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def area(self):
        """This method defines area:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This method validates value:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        else:
            self.name = name
            self.value = value
