#!/usr/bin/python3
import sys
print(f"Number of arguments: {len(sys.argv)}")
if len(sys.argv) == 0:
    print(".")
else:
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
