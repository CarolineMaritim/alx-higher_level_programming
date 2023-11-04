#!/usr/bin/python3
"""function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):

    for item in range(len(matrix)):
        for item2 in range(len(matrix[item])):
            print("{:d}".format(matrix[item][item2]), end="")
            if item2 != (len(matrix[item]) - 1):
                print(" ", end="")
        print("")
