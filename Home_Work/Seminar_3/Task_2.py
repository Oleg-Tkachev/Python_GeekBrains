#
#  В файле находятся названия фруктов.
#  Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

bykva = input("Введите первую букву фрукта: ")


with open("frukt.txt", 'r', encoding='utf-8') as data:
    fruit = data.readline().split(', ')
for fr in fruit:
    if fr[0].lower() == bykva.lower():
        print(fr)


