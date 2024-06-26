#!/usr/bin/python3
"""Defines a funtion that appends a string."""


def append_write(filename="", text=""):
    """
    This session appends a string to the
    end of a UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
