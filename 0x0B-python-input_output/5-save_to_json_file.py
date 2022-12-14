#!/usr/bin/python3
"""Write an object to a text file using  a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Save to a file using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as new:
        new.write(json.dumps(my_obj))
