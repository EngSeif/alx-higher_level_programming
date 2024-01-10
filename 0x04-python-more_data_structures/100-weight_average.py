#!/usr/bin/python3
def weight_average(my_list=[]):
    Num = 0
    Dem = 0
    if my_list == []:
        return 0
    for E in my_list:
        Num += E[0] * E[1]
        Dem += E[1]
    return Num/Dem
