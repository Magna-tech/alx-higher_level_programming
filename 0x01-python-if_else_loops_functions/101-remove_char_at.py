#!/bin/usr/python3
def remove_char_at(str, n):
    for i in str:
        if i == n:
            continue
        copy[i] = str[i]
    return copy
