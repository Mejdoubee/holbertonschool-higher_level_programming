#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                quotient = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                quotient = 0
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                quotient = 0
            finally:
                result.append(quotient)
    finally:
        return result
