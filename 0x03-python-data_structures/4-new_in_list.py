#!/usr/bin/python3


"""function that replaces an element in a list at
a specific position without modifying the original list"""


def new_in_list(my_list, idx, element):

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    dup = [i for i in my_list]
    dup[idx] = element
    return (dup)
