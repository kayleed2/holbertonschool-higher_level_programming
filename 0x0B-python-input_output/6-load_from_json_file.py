#!/usr/bin/python3
"""This module contains function load_from_json_file"""


import json


def load_from_json_file(filename):
    """Function load_from_json_file creates an object
    from a "JSON file"""
    with open(filename) as f:
        return json.load(f)
