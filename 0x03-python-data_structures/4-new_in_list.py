#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis = my_list[:]
    if 0 <= idx < len(my_list):
        lis[idx] = element
    return lis
