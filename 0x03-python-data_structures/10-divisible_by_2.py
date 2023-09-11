#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    flags = []
    for num in my_list:
        if num % 2 == 0:
            flags.append(True)
        else:
            flags.append(False)
    return(flags)
