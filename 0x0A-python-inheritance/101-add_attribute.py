#!/usr/bin/python3
# riks
"""This code defines a function attributes"""


def add_attribute(obj, att, value):
    """Code adds a new attribute to an object if possible.
    Raises:
        TypeError: Shows when the attribute cant be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
