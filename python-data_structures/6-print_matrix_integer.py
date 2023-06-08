#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for i in range(len(raw)):
            if i == len(raw) - 1:
                print("{}".format(raw[i]))
            else:
                print("{}".format(raw[i]), end=' ')
