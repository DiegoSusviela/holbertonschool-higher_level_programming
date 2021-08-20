#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import urllib.request as request
import urllib.error as error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as er:
        print("Error code: {:}".format(er.code))
