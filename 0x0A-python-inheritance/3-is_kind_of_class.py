#!/usr/bin/python3
"""To define a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """To check if an object is an instance,
    or inherited instance of the class.

    Args:
        obj (any): Refers to the object to check.
        a_class (type): This is the class to match the type of obj to.
    Returns:
        If obj is an instance or, inherited instance of a_class: True.
        Else False.
    """
    if isinstance(obj, a_class):
        return True
    return False
