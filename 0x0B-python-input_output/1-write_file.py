#!/usr/bin/python3
"""
Defines a string to a text file that returns
the number of characters
"""


def write_file(filename="", text=""):
    """
    Code here writes a string to a UTF8
    text file.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
