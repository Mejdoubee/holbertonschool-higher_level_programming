#!/usr/bin/python3
'''
Module that defines "read_file"
'''


def read_file(filename=""):
    '''
    function that reads a text file (UTF8) and prints it to stdout
    '''
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end='')
