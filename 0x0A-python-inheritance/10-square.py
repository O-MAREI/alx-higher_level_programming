#!/usr/bin/python3
""" Module 10 - Square """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class representing a square. """

    def __init__(self, size):
        """ Class constructor """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Returns area of square"""

        return self.__size ** 2
