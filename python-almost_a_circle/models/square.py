#!/usr/bin/python3
'''
class Square that inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square that inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Class constructor
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        getter for size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter for size
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        returns string representation of an object
        '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
