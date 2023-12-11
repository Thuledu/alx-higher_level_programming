#!/usr/bin/python3

# 13-main.py
"""
Main script to demonstrate the usage of Square class with to_dictionary method
"""

from models.square import Square

if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2_data = s2.to_dictionary()
    s2 = Square(**s2_data)
    print(s2)
    print(s1 == s2)
