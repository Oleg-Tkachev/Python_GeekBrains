# Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint
import numpy as np

size_matrix = int(input('Введите размер матрицы: '))
matrix = [0] * size_matrix


def create_matrix(size):
    for i in range(size):
        matrix[i] = list(randint(1, 100) for s in range(size))
    return matrix


def sum_row(matrix):
    a = np.array(matrix)
    max_sum_row = []
    for i in range(len(matrix)):
        m = (sum(a[i]))
        max_sum_row.append(m)
    return max_sum_row


def sum_diagonal(mtr):
    count = 0
    for i in range(len(mtr)):
        for j in range(len(mtr)):
            if i == j:
                count += mtr[i][j]
    return count


def res(diagonal, s_row):
    s = list(filter(lambda x: x > diagonal, s_row))
    print(f'Сумма строк превосходящих сумму главной диагонали {s}')


def Print(matrix):
    print(f'Матрица {size_matrix} * {size_matrix}: ')
    for i in range(size_matrix):
        for j in range(size_matrix):
            print(str(matrix[i][j]).rjust(3), end=' ')
        print()
    print()
    return


create_matrix(size_matrix)
Print(matrix)
print(f'Сумма строк матрицы: {sum_row(matrix)} ')
array = sum_row(matrix)
print(f'Сумма главной диагонали: {sum_diagonal(matrix)}')
line = sum_diagonal(matrix)
res(sum_diagonal(matrix), sum_row(matrix))


def indx(lin, array):
    d = [0]
    for i in range(len(array)):
        if array[i] > lin:
            print(f'Строка с суммой [{array[i]}] стоит на ==>  [{array.index(array[i])+1}] строке')


indx(line, array)


#
# Введите размер матрицы: 5
# Матрица 5 * 5:
#  21  81  86  19  62
#  60  85  39  74  70
#  71   9  81   4  45
#  39  81  71  91  84
#  60  39  15  54  29
#
# Сумма строк матрицы: [269, 328, 210, 366, 197]
# Сумма главной диагонали: 307
# Сумма строк превосходящих сумму главной диагонали [328, 366]
# Строка с суммой [328] стоит на ==>  [2] строке
# Строка с суммой [366] стоит на ==>  [4] строке
