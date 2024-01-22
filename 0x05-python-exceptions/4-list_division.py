#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    NewList = []
    Q = 0
    for i in range(0, list_length):
        try:
            Q = my_list_1[i] / my_list_2[i]
        except(ValueError, TypeError):
            print("wrong type")
            Q = 0
        except IndexError:
            print("out of range")
            Q = 0
        except ZeroDivisionError:
            print("division by 0")
        finally:
            NewList.append(Q)
    return NewList

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
