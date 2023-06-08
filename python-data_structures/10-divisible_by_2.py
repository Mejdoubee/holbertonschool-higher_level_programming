#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return list(map(lambda num: num % 2 == 0, my_list))
