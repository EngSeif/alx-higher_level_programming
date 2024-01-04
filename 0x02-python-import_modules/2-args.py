#!/usr/bin/python3

if __name__ == "__main__":
    """Print Command Line Argument"""
    import sys
    NumArgs = len(sys.argv) - 1
    if NumArgs == 1:
        print("{} argument:".format(NumArgs))
    elif NumArgs == 0:
        print("{} arguments.".format(NumArgs))
    else:
        print("{} arguments:".format(NumArgs))
    for i in range(1, NumArgs + 1):
        print("{}: {}".format(i, sys.argv[i]))
