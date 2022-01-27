#!/usr/bin/python3
"""Module with base class Base that will serve as base class for
following projects"""


import json
import sys
import os.path


class Base:
    """This class is base of all other classes in "almost a circle project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            new_list = []

        else:

            for el in list_objs:
                new_list = Base.to_json_string(el.to_dictionary())

                if os.path.exists(f'{type(el).__name__}.json'):
                    with open(f'{type(el).__name__}.json', 'a') as f:
                        f.write(new_list)

                else:
                    with open(f'{type(el).__name__}.json', 'w') as f:
                        f.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            new_list = []
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 2, 3)
        dummy.update(**dictionary)
        return dummy
