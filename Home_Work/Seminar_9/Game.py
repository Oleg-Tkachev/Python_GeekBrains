
from random import randint


start_game = False


def game_unknown_number(num, text):
    digi = randint(1, 1001)
    print(digi)
    count = 1
    while True:
        num = int(input("Введите число: "))
        if digi > num:
            text = (f"Число больше, {num}")
            count += 1
        elif digi < num:
            (f"Число меньше, {num}")
            count += 1
        else:
            resalt = f'Ура!!! Я загадал число: {digi} понадобилось: {count} попыток')
            break
            return resalt

