#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if number < 0:
    last = -last

print(f"Last digit of {number:d} is {last:d}", end=" ")

if (last == 0):
    print("and is 0")
elif (last < 6):
    print("and is less than 6 and not 0")
elif (last > 5):
    print("and is greater than 5")