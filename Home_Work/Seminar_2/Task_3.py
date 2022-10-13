# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

string_1 = input('Введите строку 1: ')
string_2 = input('Введите строку 2: ')


def Find_symbol(string_1, string_2):
    count = 0
    for i in range(len(string_1)):
        for j in range(len(string_2)):
            if string_1[i] == string_2[j]:
                count += 1

    print(f"Символ '{string_1[i]}' встречается: {count} раз")


print(Find_symbol(string_1, string_2))


###############################
# for symbol in set(string_1):
#     print(symbol, "встречается", string_2.count(symbol), "раз")
