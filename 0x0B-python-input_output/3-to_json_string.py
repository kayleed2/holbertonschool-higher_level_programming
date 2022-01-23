#!/usr/bin/python3
"""This module contains function to_json_string"""


import json


def to_json_string(my_obj):
    """Function to_json_string returns the JSON
    representation of an object"""
    return json.dumps(my_obj)
