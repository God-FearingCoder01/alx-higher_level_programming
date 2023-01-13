#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        my_list_final = []
        for my_list_element in my_list:
            if my_list_element == search:
                my_list_final.append(replace)
                continue
            my_list_final.append(my_list_element)
        return my_list_final
