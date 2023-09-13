#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for item in my_list:
        if item == search:
            index = my_list.index(search)
            my_list.remove(search)
            my_list.insert(index, replace)

    return(my_list)
