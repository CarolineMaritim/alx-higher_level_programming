#!/usr/bin/python3


"""program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys

    total = 0
    """loop through the args"""

    for index in range(len(sys.argv) - 1):
        total += int(sys.argv[index + 1])
    print("{}".format(total))
