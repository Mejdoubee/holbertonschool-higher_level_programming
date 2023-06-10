#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i**2 for i in raw] for raw in matrix]


'''
    new_list = []
    for raw in matrix:
        new = []
        for i in range(len(raw)):
            new.append(raw[i] ** 2)
        new_list.append(new)
    return new_list
'''
