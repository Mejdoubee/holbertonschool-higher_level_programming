#!/usr/bin/python3
'''
Module that define "Base" class
'''
import json


class Base:
    '''
    "Base" class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Class constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        staticmethod:
            that returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        class method:
            that writes the JSON string representation of list_objs to a file
        '''
        try:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        except TypeError:
            list_dict = []

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''
        static method:
            that returns the list of the JSON string representation json_string
        '''
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        class method:
        that returns an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        class method:
            that returns a list of instances
        '''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**dict_obj) for dict_obj in list_dicts]
