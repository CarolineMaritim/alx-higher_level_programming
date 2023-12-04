#!/usr/bin/python3
"""Function that checks instance of a specified class"""


def is_same_class(obj, a_class):

    if type(obj) == a_class:
        return True
    return False
