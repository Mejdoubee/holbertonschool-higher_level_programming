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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''
    Rectangle class that inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''
        Instantiation of Rectangle class
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
