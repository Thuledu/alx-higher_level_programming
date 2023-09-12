#!/usr/bin/python3
def class_to_json(obj):
    description = {}
    
    # Get all the attributes of the object
    attributes = obj.__dict__

    # Iterate over each attribute
    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value
    
    return description

