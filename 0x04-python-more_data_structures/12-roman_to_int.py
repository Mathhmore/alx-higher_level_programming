#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 'I'
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    for i in reversed(roman_string):
        if i in dic:
            num += dic[i]
        if dic[prev] > dic[i]:
            num -= 2 * dic[i]
        prev = i
    return num
