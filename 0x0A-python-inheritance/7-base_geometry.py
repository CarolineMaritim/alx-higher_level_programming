#!/usr/bin/python3
"""BaseGeometry class with area and int validator"""


class BaseGeometry:
    """Parent Class BaseGeometry"""

    def area(self):
        """Raises exception error mentioned"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks integer value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
