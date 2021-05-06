#!/usr/bin/python3
def print_sorted_dictionary(dic):
    for key in sorted(dic):
        print("{}: {}".format(key, dic[key]))
