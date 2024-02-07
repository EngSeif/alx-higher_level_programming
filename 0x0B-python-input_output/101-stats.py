#!/usr/bin/python3
"""
This Script:
    -   reads stdin line by line and computes metrics
    -   Each 10 lines and after a keyboard interruption
        (CTRL + C), prints those statistics since the beginning
"""

import sys

def compute_metrics():
    total_file_size = 0
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        lines_processed = 0
        for line in sys.stdin:
            lines_processed += 1
            try:
                line = line.split()
                status_code_str = line[-2]
                file_size_str = line[-1]
                status_code = int(status_code_str)
                file_size = int(file_size_str)
                total_file_size += file_size
                status_code_count[status_code] += 1
            except ValueError:
                continue
            
            if lines_processed % 10 == 0:
                print_metrics(total_file_size, status_code_count)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_count)
        raise

def print_metrics(total_file_size, status_code_count):
    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f'{status_code}: {status_code_count[status_code]}')

if __name__ == "__main__":
    compute_metrics()