#!/usr/bin/python3
"""defines number_of_lines"""


def number_of_lines(filename=""):
    """omegalul empty"""
    with open(filename, 'r', encoding='utf-8') as file:
        ret = 0
        for line in file:
            ret += 1
        return ret
