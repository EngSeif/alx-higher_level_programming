#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    NewD = a_dictionary.copy()
    for k, v in NewD.items():
        NewD[k] = v * 2    
    return NewD

def print_sorted_dictionary(a_dictionary):
    for k, i in sorted(a_dictionary.items()):
        print("{}: {}".format(k, i))

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)