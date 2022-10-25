# Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

n = int(input("Введите количество элементов массива: "))
numbers = [random.randint(1, 10) for i in range(n)]
print(numbers)

s = int(input("Напечатать элементы больше какой цифры?: "))


def numbers_greater_five(numbers):
    return list(filter(lambda x: x > s, numbers))

print(numbers_greater_five(numbers))
