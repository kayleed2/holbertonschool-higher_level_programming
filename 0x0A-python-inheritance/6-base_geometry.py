#!/usr/bin/python3
"""This module contains  a class BaseGeometry
(based on 5-base_geometry.py:
python3 -c 'print(__import__("my_module").__doc__)'"""


class BaseGeometry():
    """This class is based on 5-base_geometry.py:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def area(self):
        raise Exception('area() is not implemented')
