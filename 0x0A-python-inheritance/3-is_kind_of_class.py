#!/usr/bin/python3
"""This module contains function is_kind_of_class:
python3 -c 'print(__import__("my_module").__doc__)'"""


def is_kind_of_class(obj, a_class):
    """This function is_kind_of_class returns True
    the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    return (isinstance(obj, a_class))  # or (type(a_class) == type(obj))
