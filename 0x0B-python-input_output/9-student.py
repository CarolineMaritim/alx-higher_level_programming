#!/usr/bin/python3
"""class Student"""


class Student:
    """Parent class"""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary rep of stdnt"""
        return self.__dict__
