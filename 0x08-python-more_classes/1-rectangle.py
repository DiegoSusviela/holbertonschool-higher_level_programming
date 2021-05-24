#!/usr/bin/python3
"Defines a class Rectangle"


class Rectangle:
    """omegalul representation"""
    def __init__(self, width=0, height=0):
        """Initializes the omegalul"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width of omegalul"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width of omegalul"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height of omegalul"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height of omegalul"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
