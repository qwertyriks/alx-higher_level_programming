#!/usr/bin/python3
# By riks
"""This defines the  Square class
inhrited from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class props in constructor initialization
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This shall return width size"""
        return self.width

    @size.setter
    def size(self, value):
        """Square's height and width"""
        self.width = value
        self.height = value

    def __str__(self):
        """Class string of square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Here, this updates square properties"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary of class properties"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
