# Дан массив. С помощью цикла переписать его элементы в другой массив такого же размера следующим  образом:
# сначала должны  идти все  отрицательные  элементы,
# а  затем  все остальные. Использовать  только  один  проход  по исходному массиву.


from random import randint

numbers_no_sort = []
for i in range(10):
    numbers_no_sort.append(randint(-10, 11))
print('Несортированный масиив:')
print(numbers_no_sort)
print('Сортированный масиив:')
numbers_no_sort.sort()
print(numbers_no_sort)


################################# Второй способ #############################
# В задаче не указано можно ли менять элементы местами !
# Ниже элементы не меняются по возрастанию


numbers_positive = []
numbers_negative = []


for i in numbers_no_sort:
    if i < 0:
        numbers_negative.append(i)
    else:
        numbers_positive.append(i)


print('Несортированный масиив:')
print(numbers_no_sort)
print('Сортированный масиив:')
print(numbers_negative + numbers_positive)
