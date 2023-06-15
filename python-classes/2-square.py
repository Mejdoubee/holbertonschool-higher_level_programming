#!/usr/bin/python3
"""
Author: [Ismail Mejdoub]
Date: [06/14/2023]
Description: This module defines the Square class.
"""


class Square:
    """
    A class that represents a square.

    """

    def __init__(self, size=0):
        """
        Initialize a new Square:
        Args:
            size (int): The size of the new Square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
