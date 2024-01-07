#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(mylist) - 1):
        return None
    for indx, element in enumerate(my_list):
        if indx is idx:
            return my_list[indx]
