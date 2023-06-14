#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    c = 0
    for k in a_dictionary:
        if k == key:
            a_dictionary[k] = value
            c = 1
            break
    if c != 1:
        a_dictionary[key] = value
    return a_dictionary
