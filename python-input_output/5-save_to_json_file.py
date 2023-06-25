#!/usr/bin/python3
'''
Module that define save_to_json_file
'''
import json
to_json = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    '''
    function that writes an Object to a text file, using a JSON representation
    '''
    with open(filename, 'w', encoding='utf8') as f:
        f.write(to_json(my_obj))
