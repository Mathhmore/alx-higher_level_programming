#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        if i not in set(set_2):
            new_set.append(i)
    for k in set_2:
        if k not in set(set_1):
            new_set.append(k)
    return new_set
