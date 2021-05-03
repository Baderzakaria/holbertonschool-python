#!/usr/bin/python3
""" def print_matrix_integer(matrix=[[]]):
    for i in len(matrix):
        for j in len(matrix[i]):
            print(matrix[i][j]) """
def print_matrix_integer(matrix = [[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{}'.format(matrix[i][j]),end=' ')
        print(' ')