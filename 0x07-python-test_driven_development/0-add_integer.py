#!/usr/bin/python3
"""
Module 0-add_integer
contains a method to do sum of two numbers
"""


def add_integer(a, b=98):
    """
    adds two integer by casting it in to int if a and/or b is/are float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
