#!/usr/bin/python3
# riks
"""The class MyInt will inherit from int."""


class MyInt(int):
    """Represents the body MyInt class """

    def __eq__(self, value):
        """This code Override == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """This code Override != operator with ==."""
        return self.real == value
