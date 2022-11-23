# Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint
import numpy as np

size_matrix = int(input('Введите размер: '))
matrix = [0] * size_matrix

for i in range(len(matrix)):
    matrix[i] = list(randint(1, 100) for s in range(size_matrix))
print(f'квадратная матрица размером {size_matrix}: ')
print(matrix)

A = np.array(matrix)
max_sum_stroki = []
for i in range(len(matrix)):
    m = (sum(A[i]))
    # print(m)
    max_sum_stroki.append(m)

print(max_sum_stroki)
print(max(max_sum_stroki))


def diagonal():
    count = 0
    for i in range(size_matrix):
        for j in range(size_matrix):
            if i == j:
                count += matrix[i][j]
    print(f' {count} диагональ')
    return count


diagonal()


def Print(matrix):
    for i in range(size_matrix):
        for j in range(size_matrix):
            print(str(matrix[i][j]).rjust(3), end=' ')
        print()
    return

Print(matrix)