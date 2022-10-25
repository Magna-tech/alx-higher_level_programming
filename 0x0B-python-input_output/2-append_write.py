#!/usr/bin/python3
"""append a string to a text file (UTF8) and return number of chars written"""


def append_write(filename="", text=""):
    """Takes in filename and text as the parameter"""
    with open(filename, 'a', encoding="utf-8") as new:
        return new.write(text)
