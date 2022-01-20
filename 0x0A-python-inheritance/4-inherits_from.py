#!/usr/bin/python3
"""This module contains function inherits_from:
python3 -c 'print(__import__("my_module").__doc__)'"""


def inherits_from(obj, a_class):
    """This function inherits_from returns
    True if the object is an instance of a class
    that inherited (directly or indirectly) from
    the specified class:
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class != a_class
