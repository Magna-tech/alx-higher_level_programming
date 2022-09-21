#!/usr/bin/python3
for i in range(100):
    if i % 10 > int(i / 10):
        if i < 89:
            print("{:0>2d}".format(i), end=", ")
        else:
            print(f"{i}")
