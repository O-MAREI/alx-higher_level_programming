#!/usr/bin/python3
""" Module 1 - MyList """


class MyList(list):
    """ MyList inherits from list """

    def print_sorted(self):
        """ Prints list of attributes, sorted. """

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
