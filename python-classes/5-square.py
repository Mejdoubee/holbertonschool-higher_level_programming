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
    def __init__(self, size=0):
        """
        Initialize a new Square:
        Args:
            size (int): The size of the new Square.
        """
        self.__size = size

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
            for i in range(self.__size):
                print(f"{'#' * self.__size}")
