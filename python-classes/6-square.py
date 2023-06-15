#!/usr/bin/python3
"""
This module defines the Square class.

Author: [Ismail Mejdoub]
Date: [06/15/2023]
"""


class Square:
    """
    A class that represents a square. This class has a method for calculating
    the area of the square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square:
        Args:
            size (int): The size of the new Square.
            position (int): tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        size getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #.

        Returns:
            square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
