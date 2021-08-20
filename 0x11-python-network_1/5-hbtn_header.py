#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('x-request-id'))
