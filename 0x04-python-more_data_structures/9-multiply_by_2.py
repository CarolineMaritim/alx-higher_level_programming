#!/usr/bin/python3

""" function that returns a new dictionary with all values
multiplied by 2"""


def multiply_by_2(a_dictionary):

    return ({idx: a_dictionary[idx] * 2 for idx in a_dictionary})
