#!/usr/bin/python3
"""Defines JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """
    will returns the JSON representation
    of an object(string)
    """

    return json.dumps(my_obj)
