#!/usr/bin/python3
"""script adds args to list"""

from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

if path.exists("add_item.json") is False:
    save_to_json_file([], "add_item.json")
filename = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    filename.append(argv[i])
save_to_json_file(filename, "add_item.json")
