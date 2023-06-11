#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary_copy = a_dictionary.copy()
    for keys, values in a_dictionary_copy.items():
        if a_dictionary[keys] == value:
            del a_dictionary[keys]
    return a_dictionary
