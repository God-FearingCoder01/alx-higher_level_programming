#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str = "{:d}"
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            if j == (matrix_columns-1):
                print(str.format(matrix[i][j]))
                continue
            print(str.format(matrix[i][j]), end=" ")
