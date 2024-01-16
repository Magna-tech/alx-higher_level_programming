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
        self.validate("width", width)
        self.validate("height", height)
        self.validation("x", x)
        self.validation("y", y)


        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validate("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validate("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validation("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validation("y", y)
        self.__y = y

    def validate(self, name, value):
        """Checks if the values are not integers and <= 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")
        elif value <= 0:
            raise ValueError(f"{name} must be > 0.")

    def validation(self, name, value):
        """checks if values are integers and < 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0.")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
