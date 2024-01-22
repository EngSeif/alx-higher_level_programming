#!/usr/bin/python3
def safe_print_division(a, b):
    Q = 0
    try:
        Q = a / b
    except ZeroDivisionError:
        Q = None
    finally:
        print("Inside result: {}".format(Q))
    return Q
