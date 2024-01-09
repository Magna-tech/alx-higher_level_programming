#!/usr/bin/python3
"""An improved class"""


class BaseGeometry:
    """Area function that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """Function that validates value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
