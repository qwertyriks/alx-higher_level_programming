#!/usr/bin/python3
"""The Rectangle inheritance from the Base class"""


from models.base import Base


class Rectangle(Base):
    """The Rectangle class inherits Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method returns private attribute (__width)"""

        return self.__width

    @width.setter
    def width(self, value):
        """Here sets private attribute (__width)"""

        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """This method returns private attribute (___height)"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets private attribute (__height)"""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """private attribute (__x) is returned"""
        return self.__x

    @x.setter
    def x(self, value):
        """Private attribute (__x) is been set"""
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """We return private attribute (__y)"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set private attribute (__y)"""
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """The area of the rectangles (height*width)
        is returned"""
        return (self.height * self.width)

    def display(self):
        """This prints to standardd_output
        representation of the rectangle"""
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """The arguments props in the class been updated"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Dictionary representationof the class
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
