#!/usr/bin/python3
from calculator_1 import add, sub, mul

def magic_calculation(a, b):
    if a > b:
        return a - b
    elif a < b:
        return a + b
    else:
        return a * b
