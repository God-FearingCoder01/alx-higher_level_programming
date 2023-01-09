#!/usr/bin/python3
def get_max_int_element(list):
    max_element = list[0]
    for element in list:
        if element > max_element:
            max_element = element
    return max_element


def max_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len:
        return get_max_int_element(my_list)
    else:
        return None
