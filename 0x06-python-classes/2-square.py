#!/usr/bin/python3
# By riks
"""This is Square class defination."""


class Square:
    """The Square class body"""

    def __init__(self, size=0):
        """The Square class contructor
        Args:
            size (int): This's size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
