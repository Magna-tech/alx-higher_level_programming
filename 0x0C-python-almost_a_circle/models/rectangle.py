#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class for the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the id value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """This class inherits from the base class"""
    _width = 0
    _height = 0
    _x = 0
    _y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """We initialize the values"""
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        super().__init__(id)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
