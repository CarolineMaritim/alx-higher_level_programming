#!/usr/bin/python3

"""function that returns a tuple with the length of
a string and its first character"""


def multiple_returns(sentence):
    """check if sentence is empty"""
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
