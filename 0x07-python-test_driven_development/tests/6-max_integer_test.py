#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        ordered = [4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(max_integer(ordered), 10)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_item_list(self):
        item = [10]
        self.assertEqual(max_integer(item), 10)

    def test_string(self):
        string = "Bohemian Rhapsody"
        self.assertEqual(max_integer(string), 's')


if __name__ == '__main__':

    unittest.main()
