#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for i in new:
        new = list(map(lambda x: x*2, i))
        print(new)
