#!/usr/bin/python3

"""function that adds all unique integers in a list
(only once for each integer)"""


def uniq_add(my_list=[]):

    my_sum = 0
    for i in set(my_list):
        my_sum += i
    return (my_sum)
