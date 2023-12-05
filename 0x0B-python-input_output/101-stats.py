#!/usr/bin/python3
"""A cript that reads stdin line by line and computes metrics."""

import sys

def print_statistics(total_size, status_codes):
    """
    Prints the statistics based on the total file size and the number of lines for each status code.

    Args:
    - total_size: The total file size.
    - status_codes: A dictionary containing the number of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                parts = line.split()
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except Exception:
                pass

            if i % 10 == 0:
                print_statistics(total_size, status_codes)

            except KeyboardInterrupt:
                print_statistics(total_size, status_codes)
                raise
