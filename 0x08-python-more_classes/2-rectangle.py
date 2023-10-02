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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Get the area."""
        return(self.width * self.height)

    def perimeter(self):
        """Get the perimeter"""
        fi height == 0 or width == 0:
            return (0)
        height = self.height
        width = self.width
        return(2 * (height + width))
