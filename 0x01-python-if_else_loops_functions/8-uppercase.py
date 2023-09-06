#!/usr/bin/python3

def uppercase(str):
    for i in range(0, length(str)):
        if (i != length(str) - 1):
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(chr(ord(str[i]) - 32)))
