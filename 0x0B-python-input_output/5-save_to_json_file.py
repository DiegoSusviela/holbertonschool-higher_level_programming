#!/usr/bin/python3
""" "to_json_string" function"""


import json


def save_to_json_file(my_obj, filename):
    """omegalul epa"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
