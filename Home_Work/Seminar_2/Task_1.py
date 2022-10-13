#
# Программа, которая принимает на вход число N
# и выдает список факториалов для чисел от 1 до N.
#
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))

def Factorial(number):
    if number == 0:
        return 1
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

print(f'факториал {n}! = {Factorial(n)}')



########### Второй способ через рекурсию  ###################

def Factorial(number):
    if number == 0:
        return 1
    return number * Factorial(number - 1)


print(Factorial(n))
