#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        hold_max = my_list[0]
        for i in my_list:
            if hold_max < i:
                hold_max = i
            return hold_max
    else:
        return None
