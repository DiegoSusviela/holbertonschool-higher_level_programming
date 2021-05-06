#!/usr/bin/python3
def uniq_add(my_list=[]):
    ret = 0
    for i in set(my_list):
        ret += i
    return ret
