#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary:
        if a_dictionary[i] == value:
            del i
    return a_dictionary
