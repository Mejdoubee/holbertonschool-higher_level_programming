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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(str(name)))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))
