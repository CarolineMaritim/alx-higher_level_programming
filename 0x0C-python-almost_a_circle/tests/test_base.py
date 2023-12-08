#!/usr/bin/python3
"""unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """unittests for base.py"""

    def test_baseid(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(6, Base(6).id)


class TestBase_to_jsonstring(unittest.TestCase):
    """unittests for json strings"""

    def test_to_json_string_rectangle(self):
        rectangle = Rectangle(20, 6, 3, 5, 7)
        self.assertEqual(str, type(Base.to_json_string([rectangle.to_dictionary()])))


if __name__ == "__main__":
    unittest.main()
