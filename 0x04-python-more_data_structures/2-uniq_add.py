#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    cp = set(my_list.copy())
    for i in cp:
        sum = sum + i
    return sum
