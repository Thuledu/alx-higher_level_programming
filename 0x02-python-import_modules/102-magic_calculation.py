#!/usr/bin/python3
from magic_calculation import add, sub, mul, div

def magic_calculation(a, b):
    if a > b:
        return a - b
    elif a < b:
        return a + b
    else:
        return a * b
