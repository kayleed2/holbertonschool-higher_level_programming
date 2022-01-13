#!/usr/bin/python3
"""function that prints My name is <first name> <last name>:
python3 -c 'print(__import__("my_module").__doc__)'
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>:
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')
    
    elif isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')
    
    else:
        print("My name is {} {}".format(first_name, last_name))
