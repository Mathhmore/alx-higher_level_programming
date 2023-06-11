#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i is not in "cC":
            string = string + i
    return string
