#!/usr/bin/python3
"""function that converts a roman numeral to integer"""


def roman_to_int(roman_string):

    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
       "M": 1000
    }
    n = 0
    for idx in range(len(roman_string)):
        if rom.get(roman_string[idx], 0) == 0:
            return (0)
        if (idx != (len(roman_string) -1)) and
            roman[roman_string[idx]] < roman[roman_string[idx + 1]]):
            n += roman[roman_string[idx]] * -1
        else:
            n += roman[roman_string[idx]]
    return (n)
