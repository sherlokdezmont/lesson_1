from itertools import permutations

def sign(p):
    # Подсчёт знака перестановки (чётность инверсий)
    inversions = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inversions += 1
    return (-1) ** inversions

def leibniz_determinant(matrix):
    n = len(matrix)
    total = 0
    for p in permutations(range(n)):
        term = sign(p)
        for i in range(n):
            term *= matrix[i][p[i]]
        total += term
    return total

# Пример: 3×3 матрица
A = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print("Определитель по формуле Лейбница:", leibniz_determinant(A))


