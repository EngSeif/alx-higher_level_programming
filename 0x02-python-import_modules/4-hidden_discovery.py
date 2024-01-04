#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by the compiled module"""
    import hidden_4
    names = dir(hidden_4)
    for Name in names:
        if Name[:2] != "__":
            print(Name)
