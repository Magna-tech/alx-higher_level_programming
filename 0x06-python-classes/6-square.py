#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """initializing with a private inistance"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or not all(i >= 0 for i in value) or
            not all(type(i) is int for i in value) or
            type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
