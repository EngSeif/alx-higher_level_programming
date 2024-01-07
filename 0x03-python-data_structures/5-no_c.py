#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if ord(i) != 97 and ord(i) != 67:
            new_string += i
    else:
        return new_string
