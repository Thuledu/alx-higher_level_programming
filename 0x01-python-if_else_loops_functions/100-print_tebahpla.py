#!/usr/bin/python3
ascii_value = 0

for ascii_value in range(122, 96, -1):
    char = chr(ascii_value - 32) if ascii_value % 2 != 0 else chr(ascii_value)
    print(f"{char}", end="")
print()
