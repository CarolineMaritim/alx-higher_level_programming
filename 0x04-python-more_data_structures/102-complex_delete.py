#!/usr/bin/python3
"""function that deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):

    while item in a_dictionary.values():
        for key, value in a_dictionary.items():
            if value == item:
                del a_dictionary[key]
                break
    return (a_dictionary)
