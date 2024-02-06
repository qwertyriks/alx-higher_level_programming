#!/usr/bin/python3
"""This represents the class-to-JSON funtion."""


def class_to_json(obj):
    """This returns the dictionary represntation of json."""
    return obj.__dict__
