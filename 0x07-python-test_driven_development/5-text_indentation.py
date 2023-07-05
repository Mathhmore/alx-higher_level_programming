#!/usr/bin/python3
"""
Module 5-text_indentation
contains a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function prints a text with two new lines after ., ? and :
    """
    h = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if h != "":
            print()
            h = ""
        else:
            print(i, end="")
        if i in ".?:":
            print()
            h = i
