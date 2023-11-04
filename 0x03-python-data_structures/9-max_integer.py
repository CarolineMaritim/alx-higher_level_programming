#!/usr/bin/python3
"""function that finds the biggest integer of a list"""


def max_integer(my_list=[]):

    """check if list is empty"""
    if len(my_list) == 0:
        return (None)
    large = my_list[0]
    for item in range(len(my_list)):
        if my_list[item] > large:
            large = my_list[item]
    return (large)
