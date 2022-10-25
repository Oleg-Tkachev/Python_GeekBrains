# Дан список случайных чисел.
# Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


import random

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)


def increase_numbers(numbers):
    new_num_up = [numbers[0]]
    for i in numbers:
        if i > max(new_num_up):
            new_num_up.append(i)
    return new_num_up


print(increase_numbers(numbers))
