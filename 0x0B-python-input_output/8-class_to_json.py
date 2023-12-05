#!/usr/bin/python3
"""function that returns the dictionary description for JSON 
serialization of an object"""


def class_to_json(obj):
    """main function"""
    return obj.__dict__
