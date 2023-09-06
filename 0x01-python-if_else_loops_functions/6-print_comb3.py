#!/usr/bin/python3
for i in range(0, 90):
    if (int(str(f"{i:02}")[0]) < int(str(f"{i:02}")[1])):
        if (int(str(f"{i:02}")[0]) != int(str(f"{i:02}")[1])):
            if (i != 89):
                print(f"{i:02},", end=" ")
            else:
                print(f"{i:02}")
