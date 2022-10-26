#!/usr/bin/python3
"""Return the JSON representation of an object(string)"""


import json


def to_json_string(my_obj):
    """Convert string to JSON"""
    return (json.dumps(my_obj))
