#!/usr/bin/python3
""""read_lines" function"""


def read_lines(filename="", nb_lines=0):
    """omegalul empty"""
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        count = 0
        for nb_lines in range(nb_lines):
            print(f.readline(), end="")
