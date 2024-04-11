#!/usr/bin/python3
"""Defines a function that load from json"""
import json


def load_from_json_file(filename):
    """This loads from json to file"""
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
