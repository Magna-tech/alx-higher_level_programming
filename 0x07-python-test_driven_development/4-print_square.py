#!/usr/bin/python3
"""A functon that prints a square with the character #"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
