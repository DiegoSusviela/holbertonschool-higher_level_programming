#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
