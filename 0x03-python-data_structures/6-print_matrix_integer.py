#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_lists = len(matrix)
    for i in range(matrix_lists):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]),
                  end=" "if j < len(matrix[i])-1 else "\n")
