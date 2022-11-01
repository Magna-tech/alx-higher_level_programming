#!/usr/bin/python3
"""Base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the id value"""
        if id is not None:
            self.__id = id
        else:
            self.__id = self.__nb_objects++
