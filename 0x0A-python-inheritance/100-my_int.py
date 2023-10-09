#!/usr/bin/python3
"""Module 100-my_int"""


class MyInt(int):
    """My version of the int class with
    != and == reversed
    """

    def __eq__(self, other):
        """== becomes !="""

        return super().__ne__(other)

    def __ne__(self, other):
        """!= becomes =="""

        return super().__eq__(other)
