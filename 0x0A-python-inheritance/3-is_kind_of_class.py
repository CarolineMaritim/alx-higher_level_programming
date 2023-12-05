#!/usr/bin/python3
"""Checks class inheritance"""


def is_kind_of_class(obj, a_class):
    """Function that checks if class has inheritance"""
    if isinstance(obj, a_class):
        return True
    return False
