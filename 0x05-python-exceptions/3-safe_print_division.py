#!/usr/bin/python3
"""Returns the division of a by b."""


def safe_print_division(a, b):
    try:
        d = a / b
    except (TypeError, ZeroDivisionError):
        d = None
    finally:
        print("Inside result: {}".format(div))
    return (d)
