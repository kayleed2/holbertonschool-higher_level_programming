#!/usr/bin/python3
"""Module that contains class Student based on 9-student.py"""


from re import I


class Student:
    """Defines class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def age(self):
        return self.age

    def to_json(self, attrs=None):
        if attrs == None:
            return vars(self)
        new = {}
        for el in attrs:
            try:
                new[el] = vars(self)[el]
            except Exception:
                pass
        return new
