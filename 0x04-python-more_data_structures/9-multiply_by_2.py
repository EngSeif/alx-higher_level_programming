#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    NewD = a_dictionary.copy()
    for k, v in NewD.items():
        NewD[k] = v * 2    
    return NewD
