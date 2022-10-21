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
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
