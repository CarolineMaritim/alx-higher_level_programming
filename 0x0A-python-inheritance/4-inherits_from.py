#!/usr/bin/python3
"""Checks if an object is an inherited
instance of a class."""


def inherits_from(obj, a_class):
    """func that checks if obj is an inheritance
    of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
