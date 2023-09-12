#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        description = {}
        
        # Get all the attributes of the object
        attributes = self.__dict__

        # If attrs is provided and is a list of attribute names
        if attrs and isinstance(attrs, list):
            for attr in attrs:
                if attr in attributes and isinstance(attributes[attr], (list, dict, str, int, bool)):
                    description[attr] = attributes[attr]
        else:
            # If attrs is not provided or is not a list, retrieve all attributes
            for attr, value in attributes.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    description[attr] = value
        
        return description
    
    def reload_from_json(self, json):
        # Replace all attributes of the Student instance based on the given dictionary representation
        for attr, value in json.items():
            setattr(self, attr, value)

