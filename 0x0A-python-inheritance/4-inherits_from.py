#!/usr/bin/python3
# riks
"""This does define an inherited class-checking method."""


def inherits_from(obj, a_class):
    """This verifies if an object is an inherited instance of a class.
    Args:
        obj (any): This the object to check.
        a_class (type): this the class to compare.
    Returns:
        A boolean of inheritance
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
