# Дан отсортированный массив, заполненный случайными вещественными числами.
# Найдите ближайший к среднему арифметическому максимума и минимума элемент массива.


from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(1, 50))
numbers.sort()
print(numbers)

average = sum(numbers) / len(numbers)
print('Среднее арифметическое', average)

