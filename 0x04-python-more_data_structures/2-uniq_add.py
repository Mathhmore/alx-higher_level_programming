#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    unique_sum = 0
    for i in range(len(new_list) - 1):
        for k in range(i + 1, len(new_list) - 2):
            if new_list[i] == new_list[k]:
                del new_list[i]
    for j in new_list:
        unique_sum += j
    return unique_sum
