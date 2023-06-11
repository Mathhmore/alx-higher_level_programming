#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(tuple_a) > len(tuple_b):
        r = len(tuple_b)
    else:
        r = len(tuple_a)
    for i in range(r):
        list_a[i] = list_a[i] + list_b[i]
    return tuple(list_a)
