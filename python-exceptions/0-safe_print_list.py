#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for x in range(x):
            print(f"{my_list[i]}", end="")
            i += 1
        print()
    except IndexError:
        print()
    return i
