#!/usr/bin/python3
""" Module 8 - Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class representation of rectangle. """

    def __init__(self, width, height):
        """ Class constructor """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
