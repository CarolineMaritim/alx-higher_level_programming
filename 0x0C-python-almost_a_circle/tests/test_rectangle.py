#!/usr/bin/python3
"""Unittest for class rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.Testcase):
    """Unittest for class rectangle"""

    def test_noargs(self):
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_allargs(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)


if __name__ == "__main__":
    unittest.main()
