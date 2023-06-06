#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    arg_len = len(argv)
    if arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
