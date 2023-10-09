#!/usr/bin/python3
"""Module 11 - Square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representation of square."""

    def __init__(self, size):
        """Class constructor"""

        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns area of square."""

        return self.__size ** 2
