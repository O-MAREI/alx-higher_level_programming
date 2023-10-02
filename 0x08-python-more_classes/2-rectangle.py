#!/usr/bin/python3
"""Create a Rectangle class."""

class Rectangle:
    """Definition of rectangle class"""

    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initialize the instane."""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        else:
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
        else:
            self.__width = value

    def area(self):
        """Get the area."""
        return(self.width * self.height)

    def perimeter(self):
        """Get the perimeter"""
        height = self.height
        width = self.width
        return(2 * (height + width))
