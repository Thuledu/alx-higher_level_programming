#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them to a file."""

import sys
import json
from os import path
from typing import List

def save_to_json_file(my_obj, filename):
    """
    Saves the given object to a file in JSON format.

    Args:
    - my_obj: The object to be saved.
    - filename: The name of the file to save the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """
    Loads an object from a file in JSON format.

    Args:
    - filename: The name of the file to load the object from.

    Returns:
    - The object loaded from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

args = sys.argv[1:]
filename = 'add_item.json'

if path.exists(filename):
    data = load_from_json_file(filename)
else:
    data = []

data.extend(args)
save_to_json_file(data, filename)
