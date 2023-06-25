#!/usr/bin/python3
'''
Module that defines a Square class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    class Square that inherits from Rectangle
    '''
    def __init__(self, size):
        '''
        Instantiation of sqaure class
        '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''
        Returns the area of the square
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Returns a string representation of the rectangle
        '''
        return f"[Square] {self.__size}/{self.__size}"
