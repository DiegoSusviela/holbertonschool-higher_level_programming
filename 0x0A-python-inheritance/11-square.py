#!/usr/bin/python3
"""creates class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """omegalul empty"""
    def __init__(self, size):
        """omegalul empty"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """omegalul empty"""
        return "[Square] {}/{}".format(self.__size, self.__size)
