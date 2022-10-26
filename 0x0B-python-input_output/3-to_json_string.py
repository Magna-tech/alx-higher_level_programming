#!/usr/bin/python3
"""Return the JSON representation of an object(string)"""


import json


def to_json_string(my_obj):
    """Convert string to JSON"""
    print(json.loads(my_obj))
