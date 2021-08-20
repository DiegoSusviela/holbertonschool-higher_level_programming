#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import urllib.parse as parse
import urllib.request as request
from sys import argv

if __name__ == "__main__":
	values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
