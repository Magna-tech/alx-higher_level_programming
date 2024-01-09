#!/usr/bin/python3
"""
Checks if an object is an instance of class that inherits from a given class
"""


def inherits_from(obj, a_class):
    """
    Return true if object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return issubclass(type(obj), a_class)
