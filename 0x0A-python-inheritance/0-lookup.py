#!/usr/bin/python3
"""This module contains the function lookup(obj) that returns
a list of available attributes and methods of an object:
python3 -c 'print(__import__("my_module").__doc__)'"""


def lookup(obj):
    """function lookup(obj) that returns
a list of available attributes and methods of an object:
python3 -c 'print(__import__("my_module").my_function.__doc__)"""
    return dir(obj)
