#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for idx, c in enumerate(str):
        if idx != n:
            temp = temp + c
    return temp
