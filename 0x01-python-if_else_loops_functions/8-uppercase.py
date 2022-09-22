#!/usr/bin/python3
def islower(c):
    low = ord(c)
    return low in range(97, 123)


def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32)) if islower(c) else c, end="")
    print()
