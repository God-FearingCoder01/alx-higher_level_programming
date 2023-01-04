#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)

last_digit = number % 10

if number:
    if number > 5:
        str = "and is greater than 5"
    else:
        str = "and is less than 6 and not 0"
else:
    str = "and is 0"


print(f"Last digit of {number} is {last_digit} {str}")
