#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _multiply = {}
    for key, value in a_dictionary.items():
        _multiply[key] = value * 2
    return _multiply
