
def game_unknown_number(message):
    global count
    global digit
    if count > 0:
        bot.send_message(message.chat.id, f'Введите число {digit}')
        bot.message_handler(content_types=["text"])
        if not message.text.isdigit():
            bot.send_message(message.chat.id, f'Введите число {digit}')
        elif int(message.text) == digit:
            bot.send_message(message.chat.id, f'Ура! Ты угадал число! Это была цифра: {digit}')
        else:
            count -= 1
            m = bot.send_message(message.chat.id, f'Неверно, осталось попыток: {count}')
            bot.register_next_step_handler(m, game_unknown_number)
