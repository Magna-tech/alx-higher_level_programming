#!/usr/bin/python3
"""A function that adds two integers"""


def add_integer(a, b=98):
    """add two integers with b set to a default value"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
