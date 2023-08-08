#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Perform a magic calculation based on the values of a, b, and c."""

    if a < b:
        return c
    elif c > b:
        return (a + b)
    return ((a * b) - c)
