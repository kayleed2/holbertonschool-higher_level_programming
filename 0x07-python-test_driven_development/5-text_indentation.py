#!/usr/bin/python3
""" a function that prints a text with 2 new lines after each of these characters: ., ? and :
python3 -c 'print(__import__("my_module").__doc__)'
"""


from os import sep


def text_indentation(text):
    """ a function that prints a text with 2 new lines after each of these characters: ., ? and :
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    flag = ['.', '?', ':']
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for c in text:
        if c in flag:
            print(c, end='\n')
            print()
        else:
            print(c, end="")
