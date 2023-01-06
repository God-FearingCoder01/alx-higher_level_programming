#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
signed_number = (number * -1) if (number < 0) else (number)
last_digit = signed_number % 10
if last_digit:
    if last_digit > 5:
        s = "and is greater than 5"
    else:
        s = "and is less than 6 and not 0"
else:
    s = "and is 0"
print("Last digit of {:d} is {:d} {}".format(number, last_digit, s))
