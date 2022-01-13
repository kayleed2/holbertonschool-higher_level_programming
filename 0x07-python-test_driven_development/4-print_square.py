#!/usr/bin/python3
""" a function that prints a square with the character #.
python3 -c 'print(__import__("my_module").__doc__)'
"""


def print_square(size):
    """ a function that prints a square with the character #.
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) is True and size < 0:
        raise TypeError('size must be an integer')
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
