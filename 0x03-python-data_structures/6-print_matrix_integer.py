#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column != row[len(row) - 1]:
                print("{}".format(column), end=" ")
            else:
                print("{}".format(column), end="$\n")

    print("--$\n$")
