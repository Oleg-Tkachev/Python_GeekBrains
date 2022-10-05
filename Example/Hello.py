from contextlib import nullcontext
from multiprocessing.sharedctypes import Value


print("Hello world")

a = 2
b = 1.5 
c = a + b 

print(a + b)

print(type(a))  # печатает тип данных 
print(type(b))
print(type(c))
print(c)

value = None   # переменна с пустым значением
print("Hello  \nWorld")   # \n переход на новую строку
print("{0} {1} {2}" .format(a, b, c))  # интерполяция {индексы элементов} .format()
print(f'{a} {b} {c}')    # интерполяция 




