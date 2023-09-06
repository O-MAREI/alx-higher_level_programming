#!/usr/bin/python3

def uppercase(str):
    for i in range(0, length(str)):
        if (i != length(str) - 1):
            print(chr(ord(str[i]) - 32), end="")
        else:
            print(chr(ord(str[i]) - 32))
