#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if 97 <= c and c <= 122:
            c -= 32
        print(end="{}".format(chr((c))))
