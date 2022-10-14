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


def nearest_element(numbers, average):
    found = numbers[0]
    for item in numbers:
        if abs(item - average) < abs(found - average):
            found = item
    return found


print(f'Ближайшее число к {average} в списке {numbers} является {nearest_element(numbers, average)}')
