#!/usr/bin/python3
"""Func that defines class myInt"""


class MyInt(int):
    """Parent Class myInt"""

    def __eq__(self, value):
        """returns true if equal"""
        return self.real != value

    def __ne__(self, value):
        """Returns False if not equal to value"""
        return self.real == value
