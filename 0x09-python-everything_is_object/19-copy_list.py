#!/usr/bin/python3
def copy_list(l):
    return l[:]

my_list = [1, 2, ["Hamada", "Gamal"]]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)