#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import urllib
from sys import argv

if __name__ == "__main__":
	values = {'email': argv[2]}
    data =  urllib.parse.urlencode(values).encode('ascii')
    req =  urllib.request.Request(argv[1], data)
    with  urllib.request.urlopen(req) as response:
		d = response.read()
        print(d.decode('utf-8'))
