#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    for i in args:
        try:
            res = fct(i, i+1,...)
            return res
        except IndexError as err:
            print("Exception: {}".format(err), file=sys.stderr)
            return None
