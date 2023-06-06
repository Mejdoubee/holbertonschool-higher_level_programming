#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num_arg = len(argv) - 1
    print(f"{num_arg} {'argument' if num_arg == 1
          else 'arguments'}{'.' if num_arg == 0 else ':'}")
    for i in range(1, num_arg + 1):
        print(f"{i}{':'} {argv[i]}")
