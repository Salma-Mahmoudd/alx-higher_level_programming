#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = len(i) - 1
        for j in range(n + 1):
            print("{:d}{}".format(i[j], " " if j != n else ""), end="")
        print("")
