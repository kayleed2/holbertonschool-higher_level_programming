#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    roman = dict([('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    num = 0
    for i in roman_string:
        if i in roman:
            num += roman[i]
    return num
