#!/usr/bin/python3
"""This module contains function from_json_string"""


import json


def from_json_string(my_str):
    """Function from_json_string returns an object
    represented by a JSON string"""
    f = json.loads(my_str)
    return f
