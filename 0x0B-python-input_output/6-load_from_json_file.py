#!/usr/bin/python3
"""Create an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Create an object from given file"""
    with open(filename, encoding="utf-8") as new:
        return (json.load(new))
