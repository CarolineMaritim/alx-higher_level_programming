#!/usr/bin/python3
"""function that executes a function safely"""


def safe_function(fct, *args):

    try:
        res = fct(*args)
        return (res)
    except NotSafeError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
