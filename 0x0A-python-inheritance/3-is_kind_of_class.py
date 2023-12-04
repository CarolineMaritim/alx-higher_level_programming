#!/usr/bin/python3
"""Checks class inheritance"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
