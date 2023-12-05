#!/usr/bin/python3
"""Function that defines Class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child class Square"""

    def __init__(self, size):
        """child clase instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
