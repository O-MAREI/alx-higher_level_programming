#!/usr/bin/python3
def safe_print_integer(value):
    flag = True
    try:
        print("{:d}".format(value))
    except TypeError:
        flag = False

    return (flag)
