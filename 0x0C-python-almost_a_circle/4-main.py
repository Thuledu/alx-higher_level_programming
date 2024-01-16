#!/usr/bin/python3

# 4-main.py
"""
Main script to demonstrate the usage of Rectangle class with display method
"""

from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r2 = Rectangle(2, 2)
    r2.display()
