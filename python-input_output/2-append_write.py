#!/usr/bin/python3
'''
Module that define "append_write"
'''


def append_write(filename="", text=""):
    '''
    Function that appends a string at the end of a text file (UTF8)
    Returns: the number of characters added
    '''
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
