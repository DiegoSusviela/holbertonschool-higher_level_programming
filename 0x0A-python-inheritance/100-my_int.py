#!/usr/bin/python3
"""creates class MyInt"""


class MyInt(int):
    """omegalul empty"""
    def __eq__(self, other):
        """omegalul empty"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """omegalul empty"""
        return int.__eq__(self, other)
