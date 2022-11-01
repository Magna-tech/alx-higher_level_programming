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
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """We initialize the values"""
        Rectangle.__width = width
        Rectangle.__height = height
        Rectangle.__x = x
        Rectangle.__y = y
        super().__init__(id)

    @property
    def width(self):
        return Rectangle.__width

    @width.setter
    def set_width(self):
        Rectangle.__width = width

    @property
    def height(self):
        return Rectangle.__height

    @height.setter
    def set_height(self):
        Rectangle.__height = height

    @property
    def x(self):
        return Rectangle.__x

    @x.setter
    def set_x(self):
        Rectangle.__x = x

    @property
    def y(self):
        return Rectangle.__y

    @y.setter
    def set_y(self):
        Rectangle.__y = y
