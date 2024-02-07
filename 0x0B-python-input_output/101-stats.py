#!/usr/bin/python3
"""
This Script:
    -   reads stdin line by line and computes metrics
    -   Each 10 lines and after a keyboard interruption
        (CTRL + C), prints those statistics since the beginning
"""

import sys

def Print_Data(t_size, status_dict):
    print("File size: {}".format(t_size))
    for code in sorted(status_dict.keys()):
            print("{}: {}".format(code, status_dict[code]))

def main():
    total_size = 0
    line_count = 0
    Status_Dict = dict()
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if line_count == 10:
                Print_Data(total_size, Status_Dict)
                line_count = 1
            else:
                line_count += 1
            sp_line = line.split()
            try:
                total_size += int(sp_line[-1])
                if line[-2] in valid_codes:
                    if Status_Dict.get(line[-2], -1) == -1:
                        Status_Dict[line[-2]] = 1
                    else:
                        Status_Dict[line[-2]] += 1
            except (ValueError, IndexError):
                pass
        Print_Data(total_size, Status_Dict)
    except KeyboardInterrupt:
        Print_Data(total_size, Status_Dict)
        raise

if __name__ == "__main__":
    main()
