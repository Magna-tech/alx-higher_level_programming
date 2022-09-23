#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n_args = len(sys.argv)
    if n_args == 0:
        print(0)
    else:
        sum_ = 0
        for i in range(1, n_args):
            sum_ += int(sys.argv[i])
        print(sum_)
