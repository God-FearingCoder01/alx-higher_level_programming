#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str = "{:d}"
    if matrix == [[]]:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == (len(matrix[i])-1):
                    print(str.format(matrix[i][j]))
                else:
                    print(str.format(matrix[i][j]), end=" ")
