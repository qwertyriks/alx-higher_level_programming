#!/usr/bin/python3
# riks
"""This MyList will inherit from the  class list"""


class MyList(list):
    """The class that inherits from list"""
    def print_sorted(self):
        """This gonna prints a sorted list"""
        print(sorted(self))
