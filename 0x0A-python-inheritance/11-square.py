#!/usr/bin/python3
"""Defines class square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child class Square"""

    def __init__(self, size):
        """Function that defines a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
