#!/usr/bin/python3
"""
This module provides a function add_integer(a, b)

which adds two numbers together.
"""


def add_integer(a, b=98):
    """
    Adds 2 numbers (a, b) together. Both must be int or float,Returns int sum.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
