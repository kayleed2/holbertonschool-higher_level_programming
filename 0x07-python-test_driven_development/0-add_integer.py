#!/usr/bin/python3
""" A function that adds two integers, must be integers or floats
python3 -c 'print(__import__("my_module").__doc__)'
 """


def add_integer(a, b=98):
    """add_integer - Takes in two arguments, must be int or float.
    a: integer one
    b: integer two
    Return: int: python3 -c 'print(__import__("my_module").__doc__)'
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
