#!/usr/bin/python3
"""
This module provides a function add_integer(a, b)

which adds two numbers together.
"""


def add_integer(a, b=98):
    """
    a: The first number. Must be an integer or float.
    b: The second number. Must be an integer or float. Default is 98.
    Returns: The sum of a and b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
