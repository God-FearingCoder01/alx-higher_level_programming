#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{:d}"
    for int_num in my_list[::-1]:
        print(str.format(int_num))
