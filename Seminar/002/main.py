
# Задайте двумерный массив случайных
# чисел размером 4х5. Случайные числа не должны
# повторяться.

def zadacha1():
    import random
    rows = 4
    columns = 5
    numbers = [0] * rows
    used = []

    for i in range(len(numbers)):
         numbers[i] = list(None for _ in range(columns))

    for i in range(rows):
        for j in range(columns):
            current_number = random.randint(0, 30)
            while current_number in used:
                current_number = random.randint(0, 30)
            numbers[i][j] = current_number
            used.append(current_number)

    for row in numbers:
        print(row)

# zadacha1()


# Считайте двумерный массив из файла. Найдите разницу между вторым максимальным
#  и вторым минимальным элементами массива.

def zadacha2():
    numbers = zadacha0()
    printMatrix(numbers)
    result = []
    for row in numbers:
        for el in row:
            result.append(el)

    result = list(set(result))
    result.sort()
    print(f'{result[-2]} - {result[1]} = {result[-2] - result[1]}')

# zadacha2()




# В зрительном зале 25 рядов, в каждом из которых 36 мест.
# Информация о проданных билетах должна храниться в виде
# двумерного массива, в котором номера строк соответствуют номерам
# рядов, а номера столбцов – номерам мест.
# Определите, где лучше сесть компании из M человек, если они хотят
# ряды только с K-го по N-ный.
# Все люди должны быть рядом после посадки.
# Если это невозможно, вывести соответствующее сообщение.


def zadacha3():

    import numpy as np
    seats = np.random.randint(2, size=(25, 36))

    print(seats)

    M = int(input('How many people: '))
    K = int(input('The closest row: '))
    N = int(input('The farthest row: '))
    found = False

    for i in range(K, N + 1):
        for j in range(36 - M + 1):
            if 1 not in seats[i, j : j + M + 1]:
                print(seats[i, j : j + M])
                print(i + 1, j + 1)
                found = True
            if found:
                break
        if found:
            break
    else:
        print('No seats')


# zadacha3()


#  Дан двумерный массив. Определите
# номер строки и столбца, в котором находится
# максимальный элемент.

def zadacha4():
    import numpy as np

    numbers = np.random.randint(500, size=(10, 15))

    print(numbers)

    max_i = 0
    max_j = 0

    for i in range(numbers.shape[0]):
        for j in range(numbers.shape[1]):
            if numbers[i, j] > numbers[max_i, max_j]:
                max_i, max_j = i, j

    print(max_i, max_j)


def zadacha4():
    numbers = zadacha0()
    printMatrix(numbers)
    result = []
    for row in numbers:
        for el in row:
            result.append(el)

    print(result)
    maximum = max(result)
    print(f"максимум равен {maximum}")
    max_index = result.index(maximum)
    print(f"его индекс равен {max_index}")
    rows = len(numbers)
    columns = len(numbers[0])
    print(max_index // columns + 1)
    print(max_index % columns  + 1)

zadacha4()
