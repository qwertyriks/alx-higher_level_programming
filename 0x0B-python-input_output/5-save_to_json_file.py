#!/usr/bin/python3

"""
Defines function that writes an
Object toa text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
