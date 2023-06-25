#!/usr/bin/python3
'''
Module that defines a Square class
'''


Square = __import__('10-square').Square


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
    return f"[Rectangle] {self.__size}/{self.__size}"
