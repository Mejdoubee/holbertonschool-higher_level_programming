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

    def to_json(self, attrs=None):
        '''
        Public method def to_json(self, attrs=None): that retrieves
        a dictionary representation
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved
        '''
        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    attr_dict[i] = self.__dict__[i]
            return attr_dict

    def reload_from_json(self, json):
        '''
        Public method that replaces all attributes of the Student instance
        '''
        for key, value in json.items():
            setattr(self, key, value)
