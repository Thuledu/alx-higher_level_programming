#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout."""

def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
    - filename: The name of the file to be read (default is an empty string).

    Returns:
    - None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
