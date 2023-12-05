#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”."""

import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
    - filename: The name of the JSON file to load the object from.

    Returns:
    - The Python data structure represented by the JSON in the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
