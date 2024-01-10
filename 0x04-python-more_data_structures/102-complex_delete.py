#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ToDel = []
    for k, i in a_dictionary.items():
        if i == value:
            ToDel.append(k)
    for Ke in ToDel:
        del a_dictionary[Ke]
    return a_dictionary
