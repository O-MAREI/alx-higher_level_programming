#!/usr/bin/python3
for i in range(0, 90):
    str1 = str("{:02d}".format(i))[0]
    str2 = str("{:02d}".format(i))[1]
    if (int(str1) < int(str2) and int(str1) != int(str2)):
        if (i != 89):
            print("{:02d},".format(i), end=" ")
        else:
            print("{:02d}".format(i))
