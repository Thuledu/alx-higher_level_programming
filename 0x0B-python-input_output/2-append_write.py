#!/usr/bin/python3
"""A function that appends a string at the end of a text file."""

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file in UTF-8 and return the number of characters added.

    Args:
    - filename: The name of the file to append to (default is an empty string).
    - text: The string to be appended to the file (default is an empty string).

    Returns:
    - The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
