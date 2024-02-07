#!/usr/bin/python3
"""
This Script:
    -   reads stdin line by line and computes metrics
    -   Each 10 lines and after a keyboard interruption
        (CTRL + C), prints those statistics since the beginning
"""

import sys


def Print_Data(file_size, Status_Count):
    """ Print Metrics """
    if file_size > 0:
        print("File size: {}".format(file_size))
        for status_code, count in sorted(Status_Count.items()):
            if count > 0:
                print("{}: {}".format(status_code, count))


def main():
    """ Main Function """
    total_size = 0
    Status_Count = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                Print_Data(total_size, Status_Count)
            line = line.split()
            try:
                total_size += int(line[-1])
            except (ValueError, IndexError):
                pass
            try:
                status_code = line.strip().split(" ")[-2]
                if status_code in Status_Count:
                    Status_Count[status_code] += 1
            except IndexError:
                pass
        Print_Data(total_size, Status_Count)
    except KeyboardInterrupt:
        Print_Data(total_size, Status_Count)
        raise


if __name__ == "__main__":
    main()
