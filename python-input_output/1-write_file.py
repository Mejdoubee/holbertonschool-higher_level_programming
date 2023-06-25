#!/usr/bin/python3
'''
Module that define "write_file"
'''


def write_file(filename="", text=""):
    '''
    Function that writes a string to a text file (UTF8)
    Return: the number of characters written
    '''
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
