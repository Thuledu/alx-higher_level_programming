#!/usr/bin/python3
"""A class Student that defines a student."""

class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
        - first_name: The first name of the student.
        - last_name: The last name of the student.
        - age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
        - attrs: A list of strings containing attribute names. If provided, only the specified attributes are retrieved.

        Returns:
        - A dictionary representing the Student instance with the specified attributes.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the attributes from the provided dictionary.

        Args:
        - json: A dictionary where the keys are the public attribute names and the values are the corresponding attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
