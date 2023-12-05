#!/usr/bin/python3
"""A function that returns the dictionary description with simple data structure."""

def class_to_json(obj):
    """
    Return the dictionary description with a simple data structure for JSON serialization of an object.

    Args:
    - obj: An instance of a Class with serializable attributes: list, dictionary, string, integer, and boolean.

    Returns:
    - A dictionary representing the serialized object.
    """
    return obj.__dict__
