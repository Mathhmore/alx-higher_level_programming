#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            c += 1
        print()
        return c
    except IndexError:
        print()
        return c
