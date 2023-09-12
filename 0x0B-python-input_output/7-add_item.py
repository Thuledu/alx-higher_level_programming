#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items_to_list(args):
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(args)
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    # Get the command-line arguments excluding the script name
    arguments = sys.argv[1:]
    
    # Call the function to add the arguments to the list and save it to the file
    add_items_to_list(arguments)

