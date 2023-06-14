#!/usr/bin/python3
def best_score(a_dictionary):
    mx = 0
    name = ""
    if a_dictionary == None:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > mx:
            mx = a_dictionary[i]
            name = i
    return name
