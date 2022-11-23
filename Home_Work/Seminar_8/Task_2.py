# Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint
import numpy as np

size_matrix = int(input('Введите размер матрицы: '))
matrix = [0] * size_matrix


def create_matrix(size):
    for i in range(size):
        matrix[i] = list(randint(1, 100) for s in range(size))
    print(f'квадратная матрица размером {size_matrix} * {size_matrix}: ')
    return matrix


create_matrix(size_matrix)


def sum_stroki(matrix):
    A = np.array(matrix)
    max_sum_stroki = []
    for i in range(len(matrix)):
        m = (sum(A[i]))
        max_sum_stroki.append(m)
    return max_sum_stroki


print('Сумма строк матрицы: ')
print(sum_stroki(matrix))


def diagonal():
    count = 0
    for i in range(size_matrix):
        for j in range(size_matrix):
            if i == j:
                count += matrix[i][j]
    print(f' {count} диагональ')
    return count


print('Сумма главной диагонали: ')
diagonal()


def poisk():
    for i in range(len(sum_stroki(matrix))):
        if matrix[i] > sum_stroki(matrix):
            print(matrix[i])
            matrix[i]


print(poisk())


def Print(matrix):
    for i in range(size_matrix):
        for j in range(size_matrix):
            print(str(matrix[i][j]).rjust(3), end=' ')
        print()
    return


Print(matrix)
