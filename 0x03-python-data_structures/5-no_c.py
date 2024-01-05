#!/usr/bin/python3

def no_c(my_string):
    """all characters c and C will removed be from a string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
