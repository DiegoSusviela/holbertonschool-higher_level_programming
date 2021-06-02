#!/usr/bin/python3
"""append_write function"""


def write_file(filename="", text=""):
    """omegalul empty"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
