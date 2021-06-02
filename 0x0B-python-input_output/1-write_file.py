#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """omegalul empty"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
