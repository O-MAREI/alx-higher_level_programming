#!/usr/bin/python3
""" Module 7 - BaseGeometry """


class BaseGeometry():
    """ BaseGeometry class """

    def area(self):
        """ Raises an exception with a status message """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
