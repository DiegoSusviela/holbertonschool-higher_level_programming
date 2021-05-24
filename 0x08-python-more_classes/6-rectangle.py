#!/usr/bin/python3
"Defines a class Rectangle"


class Rectangle:
    """omegalul representation"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the omegalul"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints when omegalul is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """area of omegalul"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of omegalul"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """printable representation of omegalul"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for j in range(self.__height))
        return string

    def __repr__(self):
        """string representation of omegalul for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
