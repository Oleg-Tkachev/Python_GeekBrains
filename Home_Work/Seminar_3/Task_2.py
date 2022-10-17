#
#  В файле находятся названия фруктов.
#  Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

n = input("Введите букву: ")

def find_frukt(n):
    with open('frukt.txt', 'r', encoding='utf-8') as frukt:
        fruits = [frukt.readline().strip().replace('\n', '') for i in frukt]  # Строчку подсказали коллеги.
    for fruit in fruits:                                                      # частично не понимаю что здесь происходит(
        if fruit and fruit[0] == n:
            print(fruit)

find_frukt(n)
