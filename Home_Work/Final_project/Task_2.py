# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов,
# отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.


from matplotlib import pyplot as plt
from random import randint

# Количество домов 15
houses = []
for i in range(1, 16):
    houses.append(i)

# Площадь домов ранддомно от 100 до 300 м.кв
houses_area = []
houses_area = [randint(100, 300) for i in range(len(houses))]


# Цена домов ранддомно от 50 до 100 м.кв
houses_price = []
houses_price = [randint(3000000, 20000000) for i in range(len(houses))]


# Цена за один м.кв
prices_one_meter = []
for i in range(len(houses)):
    prices_one_meter.append(round(houses_price[i]/houses_area[i]), 2)


# Лимит стоимости квадратного метра
limit_price = 50000
required_price_line = [limit_price for i in range(len(houses))]


