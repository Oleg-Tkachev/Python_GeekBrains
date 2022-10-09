
# Программа, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#
# 1 -> x > 0, y > 0

point_X = int(input("Введите значение Х: "))
point_Y = int(input("Введите значение Y: "))

if point_X > 0 and point_Y > 0:
    print("Первоя четверть")
elif point_X < 0 and point_Y > 0:
    print("Вторая четверть")
elif point_X < 0 and point_Y < 0:
    print("Третья четверть")
elif point_X > 0 and point_Y < 0:
    print("Четвертая четверть")
