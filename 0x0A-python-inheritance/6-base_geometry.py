#!/usr/bin/python3
"""Function that raises exception"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises exception error"""
        raise Exception("area() is not implemented")
