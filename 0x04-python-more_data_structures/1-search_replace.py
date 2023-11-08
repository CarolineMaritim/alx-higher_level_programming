#!/usr/bin/python3
"""function that replaces all occurrences of
an element by another in a new list"""


def search_replace(my_list, search, replace):

    n_list = my_list[:]
    for idx in range(len(n_list)):
        if n_list[idx] == search:
            n_list[idx] == replace
    return (n_list)
