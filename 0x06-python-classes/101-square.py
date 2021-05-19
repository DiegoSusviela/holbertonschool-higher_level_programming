#!/usr/bin/python3
"""asd"""


class Square:
    """asd"""
    def __init__(self, size=0, position=(0, 0)):
        """asd"""
        self.size = size
        self.position = position

    def area(self):
        """asd"""
        return self.__size ** 2

    @property
    def size(self):
        """asd"""
        return self.__size

    @size.setter
    def size(self, value):
        """asd"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """asd"""
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """asd"""
        return self.__position

    @position.setter
    def position(self, value):
        """asd"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """asd"""
        newstring = ""
        if self.__size > 0:
            for row in range(self.__position[1]):
                newstring += "\n"
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    newstring += " "
                for column in range(self.__size):
                    newstring += "#"
                newstring += "\n"
        else:
            newstring += '\n'
        return newstring[:-1]
