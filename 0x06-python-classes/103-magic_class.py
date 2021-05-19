#!/usr/bin/python3
"""asd"""
import math


class MagicClass:
    """asd"""
    def __init__(self, radius=0):
        """asd"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """asd"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """asd"""
        return 2 * math.pi * self.__radius
