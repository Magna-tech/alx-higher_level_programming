#!/usr/bin/python3
"""
Checks if an object is an instance of class that inherits from a given class
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class)
