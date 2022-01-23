#!/usr/bin/python3
"""This module contains function read_file"""


import readline


def read_file(filename=""):
    """The read_file function reads a tesxt file and prints
    to stdout"""
    with open(filename, 'r') as f:
        print(f.read())
