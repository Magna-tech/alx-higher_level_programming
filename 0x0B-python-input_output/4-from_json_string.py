#!/usr/bin/python3
"""Return the object represented by a JSON string"""


import json


def from_json_string(my_str):
    """Convert JSON string to object representation"""
    return (json.loads(my_str))
