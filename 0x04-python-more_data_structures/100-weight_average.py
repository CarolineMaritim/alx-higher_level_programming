#!/usr/bin/python3
""" returns the weighted average of all integers tuple """


def weight_average(my_list=[]):

    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    a = 0
    b = 0
    for i in my_list:
        a += (i[0] * i[1])
        b += i[1]
    return (a/b)
