#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    unique_sum = 0
    c = 0
    for i in range(len(new_list)):
        if i != len(new_list) - 1:
            for k in range(i + 1, len(new_list)):
                if new_list[i] == new_list[k]:
                    c += 1
        if c == 0:
            unique_sum += new_list[i]
        c = 0
    return unique_sum
