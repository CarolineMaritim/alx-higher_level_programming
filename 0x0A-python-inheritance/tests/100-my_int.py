#!/usr/bin/python3
"""Func that defines class myInt"""


class MyInt(int):

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
