#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """MyList Class"""

    def print_sorted(self):
        """Function that prints sorted list"""
        print(sorted(self))
