#!/usr/bin/python3
"""A function that adds two integers"""


def add_integer(a, b=98):
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    else:
        add = int(a) + int(b)
        return add
