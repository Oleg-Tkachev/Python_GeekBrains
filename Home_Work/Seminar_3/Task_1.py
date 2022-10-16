#
# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

n = int(input("Введите число N: "))


def fibonacci(n):
    a, b = 1, 1
    with open('fibonacci.txt', 'w') as ouf:
        for i in range(1, n + 1):
            ouf.write(str(i) + ' –> ' + str(a) + '\n')
            a, b = b, a + b

print(fibonacci(n))




