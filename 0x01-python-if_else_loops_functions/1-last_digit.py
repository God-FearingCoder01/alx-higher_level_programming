#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
number = (number * -1) if number < 0 else number
last_digit = number % 10
if last_digit:
    if last_digit > 5:
        strng = "and is greater than 5"
    else:
        strng = "and is less than 6 and not 0"
else:
    str = "and is 0"
print("Last digit of {:d} is {:d} {}".format(number, last_digit, strng))
