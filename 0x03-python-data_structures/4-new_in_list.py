def new_in_list(my_list, idx, element):
    lis = my_list[:]
    if <= idx < len(my_list):
        lis[idx] = element
    return lis