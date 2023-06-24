#!/usr/bin/python3
'''
BaseGeometry module
'''


class BaseGeometry:
    '''
    BaseGeometry class
    '''
    def area(self):
        '''
        Public instance method that raises an Exception with message
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Public instance method that validates value
        '''
        if not isinstance(value, int):
            raise TypeError(f"{str(name)} must be an integer")
        if value <= 0:
            raise ValueError(f"{str(name)} must be greater than 0")
