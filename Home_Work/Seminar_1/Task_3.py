
# Программа, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#
# 1 -> x > 0, y > 0

x = int(input("Введите номер четверти: "))
if x == 1:
    print("Х > 0, Y > 0")
elif x == 2:
    print("X < 0, Y > 0")
elif x == 3:
    print("X < 0, Y < 0")
elif x == 4:
    print("X > 0, Y < 0")
elif x != 1 and x != 2 and x != 3 and x != 4:
    print(f"Некорректный ввод данных, четверти с номером {x} не существует")


# Сделал решение в обратную чторону)


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
elif point_X == 0 and point_Y == 0:
    print("точка находится на оси координат Х и Y")
