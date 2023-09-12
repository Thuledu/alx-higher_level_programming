#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        description = {}
        
        # Get all the attributes of the object
        attributes = self.__dict__

        # Iterate over each attribute
        for attr, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                description[attr] = value
        
        return description

