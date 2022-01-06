#!/usr/bin/python3
def no_c(my_string):
    s1 = my_string.translate({ord('c'): None})
    s2 = my_string.translate({ord('C'): None})
    return s2
