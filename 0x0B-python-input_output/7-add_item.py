#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them to a file."""

import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]
try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

updated_data = existing_data + args
save_to_json_file(updated_data, "add_item.json")
