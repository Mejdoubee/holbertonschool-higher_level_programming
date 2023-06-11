#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_to_delete = []
    for i in a_dictionary.keys():
        if i == key:
            key_to_delete.append(i)
    for i in key_to_delete:
        del a_dictionary[i]
    return a_dictionary
