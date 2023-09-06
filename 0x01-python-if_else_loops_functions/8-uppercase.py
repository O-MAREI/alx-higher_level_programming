#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):

        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):

            if (i != len(str) - 1):
                delim = ""
            else:
                delim = "\n"

            print("{}".format(chr(ord(str[i]) - 32)), end=delim)

        else:

            if (i != len(str) - 1):
                delim = ""
            else:
                delim = "\n"

            print("{}".format(str[i]), end=delim)
