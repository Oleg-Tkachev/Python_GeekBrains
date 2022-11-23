# В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

from random import randint

count_group = int(input('Введите количество групп: '))
students_grades = [0] * count_group
grade_average = []

for i in range(len(students_grades)):
    students_grades[i] = list(randint(1, 100) for s in range(int(input(f'Введите количество студентов в {i + 1} группе :'))))

print(students_grades)


