#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Takes in filename as the parameter"""
    with open(filename, encoding="utf-8") as new:
        for line in new:
            print(line, end="")
