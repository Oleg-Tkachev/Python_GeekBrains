import random
import math

def mean(arr):
    return sum(arr) / len(arr)

def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))])
    denominator = math.sqrt(sum([(x[i] - mean_x) ** 2 for i in range(len(x))])) * math.sqrt(sum([(y[i] - mean_y) ** 2 for i in range(len(y))]))

    return numerator / denominator

# Генерация случайных величин
x = [random.randint(1, 100) for _ in range(10)]
y = [random.randint(1, 100) for _ in range(10)]

print("Случайные величины x:", x)
print("Случайные величины y:", y)
print("Корреляция Пирсона между x и y:", pearson_correlation(x, y))


# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами).
# В формуле может быть ошибки((( 