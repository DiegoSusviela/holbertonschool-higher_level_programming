#!/usr/bin/python3
"""
Adding module

This module supplies with one function, add_integer(a, b).
"""


def add_integer(a, b):
    """Returns la suma vio"""
    if type(a) is not int and type(a) is not float or a is not a:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b is not b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
