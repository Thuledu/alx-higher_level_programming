#!/usr/bin/python3

# 12-main.py
"""
Main script to demonstrate the usage of Rectangle class with to_dictionary method
"""

from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    r2_data = r2.to_dictionary()
    r2 = Rectangle(**r2_data)
    print(r2)
    print(r1 == r2)
