#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = (-1 * number) % 10
    else:
        ld = number % 10
    print(f"{ld}", end="")
    return ld
