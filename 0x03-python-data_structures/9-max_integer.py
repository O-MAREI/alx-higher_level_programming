#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    maximum = -999999999999999

    for num in my_list:
        if num > maximum:
            maximum = num

    return(maximum)
