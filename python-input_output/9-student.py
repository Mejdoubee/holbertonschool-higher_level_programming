#!/usr/bin/python3
'''
Module that define Student class
'''


class Student:
    '''
    class Student that defines a student by:
    Public instance attributes:
    first_name, last_name and age
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Instantiation ...
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Public method def to_json(self): that retrieves
        a dictionary representation
        '''
        return self.__dict__
