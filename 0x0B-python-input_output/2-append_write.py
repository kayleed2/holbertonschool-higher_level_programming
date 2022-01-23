#!/usr/bin/python3
"""This module contains function append_write"""


def append_write(filename="", text=""):
    """The append_write function appends a string and returns
    number of characters added"""
    with open(filename, 'a') as f:
        ch = f.write(text)
        return ch
