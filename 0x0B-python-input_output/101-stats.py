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
        if status_dict[code] > 0:
            print("{}: {}".format(code, status_dict[code]))

def main():
    total_size = 0
    line_count = 0
    Status_Dict = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}
    try:
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                Print_Data(total_size, Status_Dict)
                total_size = 0
                Status_Dict = {'200': 0, '301': 0, '400': 0,
                            '401': 0, '403': 0, '404': 0,
                            '405': 0, '500': 0}
            sp_line = line.split()
            try:
                total_size += int(sp_line[-1])
                status_code = sp_line[-2]
                if status_code in Status_Dict.keys():
                    Status_Dict[status_code] += 1
            except (ValueError, IndexError):
                pass
        Print_Data(total_size, Status_Dict)
    except KeyboardInterrupt:
        Print_Data(total_size, Status_Dict)
        raise

if __name__ == "__main__":
    main()
