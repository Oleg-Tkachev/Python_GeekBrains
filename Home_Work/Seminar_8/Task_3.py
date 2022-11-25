# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7- дневный промежуток этого периода.
# Выведите его даты.


from random import randint

day = 30
temperature = [0]
week = []
sum_temp = 0
n = 3            # срез по три дня, для примера

temperature = list(randint(10, 25) for i in range(day))  # Пример 30 дней с температурой от 10 до 25 градусов
print('Температура за месяц: ')
print(temperature)


temp_3days = ([temperature[i:i + n] for i in range(0, len(temperature), n)])
print('Срез данных по три дня: ')
print(temp_3days)
for sr in temp_3days:
    tmp = 0
    if sum(sr) > tmp:
        tmp += sum(sr)
        week.append(tmp)

print('Среднее значение температуры по три дня: ')
print(week)

d = max(week)
print(f'Максимальная средняя температура была {round(d / 3, 2)} градуса ')
m = week.index(d)

if m + 1 == 1:
    print('Такая погода была с 1 по 3 число')
elif m + 1 == 2:
    print('Такая погода была с 4 по 6 число')
elif m + 1 == 3:
        print('Такая погода была с 7 по 9 число')
elif m + 1 == 4:
        print('Такая погода была с 10 по 12 число')
elif m + 1 == 5:
    print('Такая погода была с 13 по 15 число')
elif m + 1 == 6:
        print('Такая погода была с 16 по 18 число')
elif m + 1 == 7:
        print('Такая погода была с 19 по 21 число')
elif m + 1 == 8:
    print('Такая погода была 22 по 24 число')
elif m + 1 == 9:
        print('Такая погода была с 25 по 27 число')
elif m + 1 == 10:
        print('Такая погода была с 28 по 30 число')




# Температура за месяц:
# [19, 13, 18, 21, 22, 24, 16, 23, 25, 15, 14, 17, 24, 11, 16, 12, 14, 13, 17, 17, 17, 23, 13, 12, 24, 20, 13, 16, 15, 21]
# Срез данных по три дня:
# [[19, 13, 18], [21, 22, 24], [16, 23, 25], [15, 14, 17], [24, 11, 16], [12, 14, 13], [17, 17, 17], [23, 13, 12], [24, 20, 13], [16, 15, 21]]
# Среднее значение температуры по три дня:
# [50, 67, 64, 46, 51, 39, 51, 48, 57, 52]
# Максимальная средняя температура была 22.33 градуса
# Такая погода была с 4 по 6 число
#
# Process finished with exit code 0












