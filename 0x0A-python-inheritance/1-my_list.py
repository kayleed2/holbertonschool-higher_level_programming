#!/usr/bin/python3
"""Creation of class MyList that inherits from list:
python3 -c 'print(__import__("my_module").__doc__)'"""


class MyList(list):
    """Class inheriting list:
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self):
        """initializes this object"""
        super().__init__()

    def print_sorted(self):
        """Prints list sorted in ascending order:
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        print(sorted(self))
