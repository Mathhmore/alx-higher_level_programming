#!/usr/bin/python3
"""
Module: 3-say_my_name
contains a function to print My name
"""


def say_my_name(first_name, last_name):
    """
    method prints My name is <first_name> <last_name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
