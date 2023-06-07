#!/usr/bin/python3
def no_c(my_string):
    string_copy = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            string_copy += i
    return string_copy
