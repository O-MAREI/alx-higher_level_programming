#!/usr/bin/python3
"""Create a Rectangle class."""


class Rectangle:
    """Definition of rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize the instane."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Get the height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the width."""
        return(self.__height)

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Get the area."""
        return(self.width * self.height)

    def perimeter(self):
        """Get the perimeter"""
        height = self.height
        width = self.width
        return(2 * (height + width))

    def __str__(self):
        """Print the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """Print the rectangle using eval."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a goodbye message at deletion."""
        print("Bye rectangle...")
