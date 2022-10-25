
# Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают.
# Список уникальных элементов [1, 4, 2, 3, 6, 7]


import random

numbers = [random.randint(1, 10) for i in range(10)]
print("Список из 10 случайных элементов от 1 до 10:")
print(numbers)

def filter_elements(numbers):
    return list(filter(lambda x: numbers.count(x) == 1, numbers))

print("Список уникальных элементов из списка выше:")

print(filter_elements(numbers))

