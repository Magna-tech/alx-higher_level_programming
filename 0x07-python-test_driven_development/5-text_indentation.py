#!/usr/bin/python3
""" a function that prints a text with 2 new lines after each of these characters: ., ? and :"""

def text_indentation(text):
    """Splits a paragraph into lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    print(text.split("."), end="\n")
