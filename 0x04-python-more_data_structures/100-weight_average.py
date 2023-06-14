#!/usr/bin/python3
def weight_average(my_list=[]):
    n = 0
    m = 1
    d = 0
    c = 0
    if len(my_list) == 0:
        return 0
    for i in list(my_list):
        for j in i:
            c += 1
            m *= j
            if c == len(i):
                k = j
        d += k
        n += m
        c = 0
        m = 1
    return n / d
