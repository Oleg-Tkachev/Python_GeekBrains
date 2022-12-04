# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from matplotlib import pyplot as plt


def zadacha_1():
    x = []
    y = []
    num_x = []
    num_y = []

    for i in range(-10, 11):
        x.append(i)

    for i in range(len(x)):
        nums = (5 * (x[i] ** 2) + 10 * x[i] - 30)
        y.append(nums)

    for i in range(len(y)):
        if y[i] < 0:
            num_x.append(x[i])
            num_y.append(y[i])

    print(x)
    print(y)
    print(num_x)
    print(num_y)

    plt.plot(x, y)
    plt.plot(num_x, num_y)
    plt.title('Отрицательные значения функция f(x)=5x^2+10x−30\n принимает при х = [-1 ± √7]')
    plt.ylabel('ось X')
    plt.xlabel('ось Y')
    plt.show()


zadacha_1()







