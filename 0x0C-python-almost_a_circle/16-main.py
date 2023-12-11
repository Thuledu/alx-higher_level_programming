#!/usr/bin/python3

# 16-main.py
"""
Main script to demonstrate the usage of Base class with to_json_string and from_json_string methods
"""

from models.base import Base

if __name__ == "__main__":
    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Base.to_json_string(list_input)
    list_output = Base.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

