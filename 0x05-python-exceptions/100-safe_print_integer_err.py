#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except Exception as ty:
        print("Exception: {}".format(ty), file=sys.stderr, end="\n")
        return False
