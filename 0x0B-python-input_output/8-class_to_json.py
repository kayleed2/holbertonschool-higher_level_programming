#!/usr/bin/python3
"""Module containing the function class_to_json"""


import json


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structure """
    return vars(obj)
