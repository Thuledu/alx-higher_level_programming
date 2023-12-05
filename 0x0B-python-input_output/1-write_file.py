#!/usr/bin/python3
"""A function that writes a string to a text file."""

def write_file(filename="", text=""):
    """
    Write a string to a text file in UTF-8 and return the number of characters written.

    Args:
    - filename: The name of the file to write to (default is an empty string).
    - text: The string to be written to the file (default is an empty string).

    Returns:
    - The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
