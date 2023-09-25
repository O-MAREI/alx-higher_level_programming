#!/usr/bin/python3
def safe_print_integer(value):
    flag = True
    try:
        print({:d}.format(value), end="\n")
    except TypeError:
        flag = False

    return (flag)
