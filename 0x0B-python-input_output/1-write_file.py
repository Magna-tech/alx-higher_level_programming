#!/usr/bin/python3
"""write a string to a text file (UTF8) and return number of chars written"""


def write_file(filename="", text=""):
    """Takes in filename as the parameter"""
    with open(filename, 'w', encoding="utf-8") as new:
        return new.write(text)
