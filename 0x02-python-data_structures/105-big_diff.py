#!/usr/bin/python3
def big_diff(my_list=[]):
    if not my_list or len(my_list) == 1:
        return 0
    big = my_list[0]
    lil = my_list[0]
    for i in my_list:
        if i > big:
            big = i
        if i < lil:
            lil = i
    return big - lil
