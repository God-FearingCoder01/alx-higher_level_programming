#!/usr/bin/python3
def no_c(my_string):
    c = chr(99)
    C = chr(67)
    string_free_of_c = ""
    for letter in my_string:
        if letter is c or letter is C:
            continue
        string_free_of_c += letter
    return string_free_of_c
