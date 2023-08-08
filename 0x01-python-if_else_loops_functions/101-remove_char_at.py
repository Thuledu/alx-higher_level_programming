#!/usr/bin/python3
def remove_char_at(str, n):
    chars = [c for i, c in enumerate(str) if i != n]
    return ''.join(chars)
