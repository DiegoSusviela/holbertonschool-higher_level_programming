#!/usr/bin/python3
"""asd"""


class Square:
    """asd"""
    def __init__(self, size=0):
        """asd"""
        self.__size = size

    def area(self):
        """asd"""
        return self.__size * self.__size

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

    def __eq__(self, other):
        """asd"""
        return(self.area() == other.area())

    def __ne__(self, other):
        """asd"""
        return(self.area() != other.area())

    def __lt__(self, other):
        """asd"""
        return(self.area() < other.area())

    def __le__(self, other):
        """asd"""
        return(self.area() <= other.area())

    def __gt__(self, other):
        """asd"""
        return(self.area() > other.area())

    def __ge__(self, other):
        """asd"""
        return(self.area() >= other.area())
