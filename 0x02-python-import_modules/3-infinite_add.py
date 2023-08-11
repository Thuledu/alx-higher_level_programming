#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
sum_result = sum(int(arg) for arg in arguments)

print(sum_result)
