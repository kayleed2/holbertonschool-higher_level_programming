#!/usr/bin/python3
"""Module that contains class Student"""


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
    
    def to_json(self):
        return vars(self)
