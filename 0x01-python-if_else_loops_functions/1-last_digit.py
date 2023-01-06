#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unsigned_number = (number * -1) if (number < 0) else (number)
last_digit = unsigned_number % 10
unsigned_last_digit = (last_digit * -1) if (number < 0) else (last_digit)
if unsigned_last_digit:
    if unsigned_last_digit > 5:
        s = "and is greater than 5"
    else:
        s = "and is less than 6 and not 0"
else:
    s = "and is 0"
print("Last digit of {:d} is {:d} {}".format(number, unsigned_last_digit, s))
