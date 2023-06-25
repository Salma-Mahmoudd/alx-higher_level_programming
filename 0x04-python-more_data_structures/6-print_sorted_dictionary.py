#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        tmp = sorted(a_dictionary.keys())
        for i in tmp:
            print("{}: {}".format(i, a_dictionary[i]))
