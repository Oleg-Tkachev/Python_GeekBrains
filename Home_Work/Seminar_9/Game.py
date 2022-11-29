
from random import randint
from Main import bot


digit = randint(1, 10)
count = 5


def game_unknown_number(mes):
    global digit
    count = 5
    global game
    bot.send_message(message.chat.id, '"УГАДАЙ ЦИФРУ"!\n Количество попыток: [5]')
    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 10 !')
    while count > 0:
        bot.send_message(message.chat.id, f'Введите число {digit}')
        bot.message_handler(content_types=["text"])
        if int(message.text) == digit:
            bot.send_message(message.chat.id, 'Ура! Ты угадал число! Это была цифра:', digit)
            break
        else:
            count -= 1
            bot.send_message(message.chat.id, 'Неверно, осталось попыток:', count)
