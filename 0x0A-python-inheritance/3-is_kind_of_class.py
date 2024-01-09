#!/usr/bin/python3
"""A function that checks if an instance is same class or inherited"""


def is_kind_of_class(obj, a_class):
    """
    Return true if object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
