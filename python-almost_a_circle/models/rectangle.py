#!/usr/bin/python3
'''
class Rectangle that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''
    Inherits class from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        "Class constructor(initialisation)"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_value(name, value, min_value=0, status=True):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if status:
            if value <= min_value:
                raise ValueError(f"{name} must be > {min_value}")
        else:
            if value < min_value:
                raise ValueError(f"{name} must be >= {min_value}")
        return (value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.validate_value(
                       "width", value, min_value=0, status=True
                       )

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.validate_value(
                        "height", value, min_value=0, status=True
                        )

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self.validate_value("x", value, min_value=0, status=False)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = self.validate_value("y", value, min_value=0, status=False)

    def area(self):
        '''
        returns the area value of the Rectangle instance
        '''
        return self.width * self.height

    def display(self):
        '''
        prints in stdout the Rectangle instance with the character #
        '''
        print('\n' * self.y, end='')
        print((' ' * self.x + '#' * self.width + '\n') * self.height, end='')

    def __str__(self):
        '''
        returns string representation of an object
        '''
        return f"[Rectangle] \
({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''
        Public method that assigns an argument to each attribute
        '''
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
        returns the dictionary representation of a Rectangle
        '''
        attributes = ['x', 'y', 'id', 'height', 'width']
        return {
            i: getattr(self, i) for i in attributes
        }
