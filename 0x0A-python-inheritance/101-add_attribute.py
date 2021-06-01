#!/usr/bin/python3
"""module"""


def add_attribute(obj, objname, value):
    """omegalul empty"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
