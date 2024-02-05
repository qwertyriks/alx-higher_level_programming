#!/usr/bin/python3
# riks
"""This Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks to see if an object is exactly an instance of
    a given class or not.

    Args:
        obj (any): Represents The object to check.
        a_class (type): Is the class to match the type of obj
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
