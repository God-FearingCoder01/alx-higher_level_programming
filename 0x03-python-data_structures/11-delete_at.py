#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list_len = len(my_list)
    idx_is_negative = (idx < 0)
    idx_out_of_range = (idx >= my_list_len)
    if idx_is_negative or idx_out_of_range:
        pass
    else:
        upperbound = my_list_len - 1
        my_list_copy = my_list
        if idx == upperbound:
            my_list_copy = my_list_copy[:idx]
        else:
            my_list_copy = my_list_copy[:idx] +\
            my_list_copy[-(upperbound - idx):]
        my_list[:] = my_list_copy
    return my_list
