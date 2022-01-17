#!/usr/bin/python3
""" a function that prints a text with
2 new lines after each of these characters: ., ? and :
python3 -c 'print(__import__("my_module").__doc__)'
"""


from lib2to3.pgen2.token import NEWLINE


def text_indentation(text):
    """ text_indentation - a function that prints a text with
    2 new lines after each of these characters: ., ? and :
    text: text to test
    Return: Nada
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    flag = ['.', '?', ':']
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    after_newline = False
    for c in text:
        if after_newline:
            if c == " ":
                continue
            after_newline = False
        if c in flag:
            print(c)
            after_newline = True
        else:
            print(c, end="")
