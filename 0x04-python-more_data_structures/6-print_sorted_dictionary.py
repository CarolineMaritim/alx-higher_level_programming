#!/usr/bin/python3
"""function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):

    [print("{}: {}".format(idx, a_dictionary[idx]))
        for idx in sorted(a_dictionary)]
