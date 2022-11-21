#!/usr/bin/python3
"""function returns a list of available attributes and methods of an object"""


def lookup(obj):
    """return a list of attributes"""
    new_list = dir(obj)
    return new_list
