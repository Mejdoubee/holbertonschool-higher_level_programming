#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    sum_arg = sum(int(arg) for arg in argv[1:])
    print(sum_arg)
