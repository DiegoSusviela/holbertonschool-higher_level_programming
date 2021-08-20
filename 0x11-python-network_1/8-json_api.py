#!/usr/bin/python3
"""alibaba y los 40 ladrones"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if len(dic.keys()) > 0:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
