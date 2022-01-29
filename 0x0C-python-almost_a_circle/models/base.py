#!/usr/bin/python3
"""Module with base class Base that will serve as base class for
following projects"""


import json
import sys
import os.path


class Base:
    """This class is base of all other classes in "almost a circle project"""
    __nb_objects = 0

    @classmethod
    def clear(cls):
        Base.__nb_object = 0

    def __init__(self, id=None):
        """Initializes Base class"""
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
        new_list = []
        if list_objs is not None:
            for el in list_objs:
                str = el.to_dictionary()
                new_list.append(str)
            json_str = cls.to_json_string(new_list)
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(json_str)

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
        dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if os.path.exists(f'{cls.__name__}.json') is False:
            return []
        with open(f'{cls.__name__}.json', 'r') as f:
                obj = cls.from_json_string(f.read())
        ls = []
        for i in obj:
            x = cls.create(**i)
            ls.append(x)
        return ls
