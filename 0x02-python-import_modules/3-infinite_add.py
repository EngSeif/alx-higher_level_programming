#!/usr/bin/python3

if __name__ == "__main__":
    """Sum Command Line Argument Numbers."""
    import sys
    NumArgs = len(sys.argv) - 1
    sum = 0
    for i in range(1, NumArgs + 1):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
