#!/usr/bin/python3
'''
Module that define save_to_json_file
'''
from_json_string = __import__('4-from_json_string').from_json_string


def load_from_json_file(filename):
    '''
    Function that creates an Object from a “JSON file”
    '''
    with open(filename, 'r', encoding='utf8') as f:
        return from_json_string(f.read())
