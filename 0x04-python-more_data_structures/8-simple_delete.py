#!/usr/bin/python3
def simple_delete(dic, key=""):
    if key in dic:
        del dic[key]
    return dic
