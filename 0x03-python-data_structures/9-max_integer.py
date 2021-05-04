#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ret = my_list[0]
        for i in my_list[1:]:
            if i > ret:
                ret = i
        return ret
