#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    sttr = ""
    for i in str:
        if j != n:
            sttr = sttr + i
        j = j + 1
    return sttr
