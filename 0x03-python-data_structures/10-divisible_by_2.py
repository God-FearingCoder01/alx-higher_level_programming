#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new_list = []
    for element in my_list:
        is_divisible_by_2 = element % 2
        if is_divisible_by_2:
            my_new_list.append(False)
        else:
            my_new_list.append(True)
    return my_new_list
