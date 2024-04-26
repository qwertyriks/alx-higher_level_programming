#!/usr/bin/python3
# by riks
"""Square class defination."""


class Square:
    """The square class body."""

    def __init__(self, size=0):
        """The square contructor.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size

    def area(self):
        """Should return the new area of the square."""
        return (self.__size * self.__size)
