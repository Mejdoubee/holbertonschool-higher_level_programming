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
