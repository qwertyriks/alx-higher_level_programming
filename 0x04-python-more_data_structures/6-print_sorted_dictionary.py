#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for s in sorted(a_dictionary.keys()):
        print("{}: {}".format(s, a_dictionary.get(s)))
