#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    str = "{:d}"
    my_list_len = len(my_list)
    if my_list_len:
        for i in range(my_list_len):
            current_index = my_list_len - (i + 1)
            print(str.format(my_list[current_index]))
    else:
        print()
