# В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
#
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»



with open('icecream', 'r', encoding='utf-8') as inf:

    icecream_range = set(inf.readline().split(', '))
    print(icecream_range)

    icecream_sklad = set(inf.readline().split(', '))
    print(icecream_sklad)

    print(icecream_range - icecream_sklad)

