#!/usr/bin/python3
import sys
import random
from time import sleep
import datetime

def compute_metrics():
    total_file_size = 0
    status_code_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            
            # Parse the line
            parts = line.strip().split()
            file_size = int(parts[-1])
            status_code = parts[-2]
            
            # Increment the total file size
            total_file_size += file_size
            
            # Increment the count for the status code
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            
            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("Total file size:", total_file_size)
                for code in sorted(status_code_counts):
                    print(code + ":", status_code_counts[code])
                print()
    except KeyboardInterrupt:
        # Print final statistics after keyboard interruption
        print("Total file size:", total_file_size)
        for code in sorted(status_code_counts):
            print(code + ":", status_code_counts[code])

compute_metrics()

