#!/usr/bin/python3
def create_list_copy(list):
    list_copy = []
    list_len = len(list)
    for i in range(list_len):
        list_copy.append(list[i])
    return list_copy


def new_in_list(my_list, idx, element):
    my_list_copy = create_list_copy(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list_copy
    else:
        my_list_copy[idx] = element
        return my_list_copy
