#!/usr/bin/python3
'''
    This module provides a function that prints:
    My name is <first name> <last name>
'''
def say_my_name(first_name, last_name=""):
    '''
        This module provides a function that

        Args:
            first_name (type string):
            last_name (type string):        
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
