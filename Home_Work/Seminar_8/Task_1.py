# В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

import operator
from functools import reduce
from random import randint
from statistics import mean
import numpy as np
from urllib3.connectionpool import xrange

count_group = int(input('Введите количество групп: '))
students_grades = [0] * count_group
grade_average = []

for i in range(len(students_grades)):
    students_grades[i] = list(
        randint(1, 100) for s in range(int(input(f'Введите количество студентов в {i + 1} группе :'))))

print(students_grades)

average_students = np.mean(students_grades, axis=1)

print(np.round(average_students))

lst = students_grades
a = lst.index(max(lst)) + 1

b = max(lst)
c = lst.index(b)
print(b)
print(c + 1)


