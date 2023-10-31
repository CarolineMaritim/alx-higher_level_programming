#!/usr/bin/python3
"""Prints numbers ranging from 0-100"""

for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{:02}".format(n), end=", ")
