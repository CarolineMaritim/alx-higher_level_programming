#!/usr/bin/python3
"""Defines a class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child Class Rectangle"""

    def __init__(self, width, height):
        """Defines a Rectangle and validates
        width and height of the same"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
