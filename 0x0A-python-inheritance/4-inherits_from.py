#!/usr/bin/python3
"""defines inherits_from function"""


def inherits_from(obj, a_class):
    """omegalul empty"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
