#!/usr/bin/python3
"""
Module defines test_indentation function
"""


def text_indentation(text):
    """splits a text with "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
