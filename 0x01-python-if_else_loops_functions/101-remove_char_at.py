#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for idx, c in enumerate(str):
        if idx != n:
            temp = temp + c
    return temp

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
