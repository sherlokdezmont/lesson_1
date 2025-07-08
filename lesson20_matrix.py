import numpy as np


def matrix(n):
    matrix_n = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix_n[i, j]= (-1) ** (i + j)
    return matrix_n

n = 4
matrix_n = matrix(n)
print(matrix_n)