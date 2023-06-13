#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i != idx:
                new_list += my_list[i]
        return new_list
