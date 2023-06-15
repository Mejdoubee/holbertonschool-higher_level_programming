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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """

        return self.__size ** 2
