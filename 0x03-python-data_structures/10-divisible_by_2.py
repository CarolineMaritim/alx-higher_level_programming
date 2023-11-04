#!/usr/bin/python3
"""function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):

    result = []
    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return (result)
