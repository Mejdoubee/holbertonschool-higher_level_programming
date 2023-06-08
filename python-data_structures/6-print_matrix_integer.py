#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        if len(raw) == 0:
            print("")
        for i in range(len(raw)):
            if i == len(raw) - 1:
                print("{:d}".format(raw[i]))
            else:
                print("{:d}".format(raw[i]), end=' ')
