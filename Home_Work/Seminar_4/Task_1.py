#  Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

n = int(input("Введите число N: "))


def list_multipliers_number(num):
    divisor = 2
    numbers = []
    while divisor <= num:
        if num % divisor == 0:
            numbers.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return numbers


print(f"{n} --> {list_multipliers_number(n)}")
