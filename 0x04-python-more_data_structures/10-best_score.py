#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    MaxV = a_dictionary.values()
    Keys = a_dictionary.keys()
    best = max(filter(lambda Keys: a_dictionary[Keys] == max(MaxV), Keys))
    return best
