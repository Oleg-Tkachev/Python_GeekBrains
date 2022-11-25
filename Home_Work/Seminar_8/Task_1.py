# В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка.
# Определите группу с наилучшим средним баллом.

from random import randint

count_group = int(input('Введите количество групп: '))
count_students_group = [0] * count_group
grade_average = []


for i in range(len(count_students_group)):
    count_students_group[i] = list(
        randint(2, 5) for s in range(int(input(f'Введите количество студентов в {i + 1} группе :'))))
print(count_students_group)
print()


for row in count_students_group:
    mean_grades = 0
    for i in row:
        mean_grades += i
        mean_grades = mean_grades / len(row)
        mean = round(mean_grades, 2)
    grade_average.append(mean)

p = max(grade_average)
s = grade_average.index(p)
print(f'Средний балл по группам: {grade_average}')
print(f'Максимум баллов [{p}] набрала группа [{s + 1}]')



# Введите количество групп: 5
# Введите количество студентов в 1 группе :5
# Введите количество студентов в 2 группе :6
# Введите количество студентов в 3 группе :3
# Введите количество студентов в 4 группе :8
# Введите количество студентов в 5 группе :9
# [[2, 3, 3, 5, 4], [3, 2, 3, 4, 4, 3], [4, 3, 3], [3, 3, 4, 3, 5, 2, 4, 3], [5, 3, 5, 4, 5, 2, 4, 2, 2]]
#
# Средний балл по группам: [1.03, 0.63, 1.48, 0.44, 0.25]
# Максимум баллов [1.48] набрала группа [3]
#
# Process finished with exit code 0

