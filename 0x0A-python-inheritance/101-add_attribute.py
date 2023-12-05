#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Func that adds new attr to an obj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
