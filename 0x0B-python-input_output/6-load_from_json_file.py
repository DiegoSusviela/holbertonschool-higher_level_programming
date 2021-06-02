#!/usr/bin/python3
""" "to_json_string" function"""

import json


def load_from_json_file(filename):
    """omegalul epa"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
