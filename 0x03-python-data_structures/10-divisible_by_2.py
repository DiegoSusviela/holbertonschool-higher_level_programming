#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis1 = []
    if my_list:
        for j in my_list:
            lis1.append(False if j % 2 else True)
    return lis1
