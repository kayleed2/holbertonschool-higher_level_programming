#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str = "Last digit of"
ls = "is less than 6 and not 0"
if number < 0:
    last_digit = last_digit * -1
if last_digit > 5:
    print("{} {} is {} and is greater than 5".format(str, number, last_digit))
elif last_digit == 0:
    print("{} {} is {} and is 0".format(str, number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} {} is {} and {}".format(str, number, last_digit, ls))
