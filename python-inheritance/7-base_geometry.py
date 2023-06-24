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
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
