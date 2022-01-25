#!/usr/bin/python3
"""Module with base class Base that will serve as base class for
following projects"""


class Base:
    """This class is base of all other classes in "almost a circle project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
