
# Программа, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8
import math


number = int(input("Введите значение N: "))
n = range(1, number + 1)
for i in n:
    if i % 2 == 0:
        print(i, end=" ")


