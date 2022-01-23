#!/usr/bin/python3
"""This module contains function write_file"""


def write_file(filename="", text=""):
    """The write_file function writes a text file and returns
    number of characters written"""
    with open(filename, 'w') as f:
        ch = f.write(text)
        return ch
