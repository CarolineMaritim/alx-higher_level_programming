#!/usr/bin/python3
"""Func that reads text files and prints in stdout"""


def read_file(filename=""):
    """Function that reads txt files
    and prints in stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
