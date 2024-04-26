#!/usr/bin/python3
# riks
"""Here defines the class BaseGeometry."""


class BaseGeometry:
    """Represents the Class body."""

    def area(self):
        """WHen Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verifies a parameter format.
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
