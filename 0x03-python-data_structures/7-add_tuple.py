#!/usr/bin/python3
def get_tuple_members(tuple_h=()):
    if len(tuple_h) == 0:
        return (0, 0)
    elif len(tuple_h) == 1:
        return (tuple_h[0], 0)
    elif len(tuple_h) >= 2:
        return (tuple_h[0], tuple_h[1])


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = get_tuple_members(tuple_a)
    new_tuple_b = get_tuple_members(tuple_b)
    tuple_entry_1 = new_tuple_b[0] + new_tuple_a[0]
    tuple_entry_2 = new_tuple_a[1] + new_tuple_b[1]
    return (tuple_entry_1, tuple_entry_2)
