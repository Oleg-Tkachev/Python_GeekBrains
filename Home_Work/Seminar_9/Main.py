# Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

# Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import requests
from telebot import types
import telebot
import time
from random import randint
from operator import truediv, mul, add, sub


bot = telebot.TeleBot("5932647150:AAGU1GllNxW4lPWnct9ynbxCEg3FWlckc7c", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('Info')
itembtn2 = types.KeyboardButton('Game')
itembtn3 = types.KeyboardButton('Погода')
itembtn4 = types.KeyboardButton('Cats')
itembtn5 = types.KeyboardButton('Юмор')
itembtn6 = types.KeyboardButton('Калькулятор')
itembtn7 = types.KeyboardButton('file')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn6, itembtn7)

digit = randint(1, 10)
count = 0

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


def Calculate(message):
    # на посторах нашел eval, очень интересная функция и она РАБОТАЕТ))))
    if '+' in message.text or '-' in message.text or '/' in message.text or '*' in message.text:
        calculate = str(eval(str(message.text)))
        bot.send_message(message.chat.id, f'{calculate}')
    else:
        bot.send_message(message.chat.id, 'Не в моих силах такое вычислить')



@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Добрый человек :) ' + message.from_user.first_name, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def Logs_programm(message, content_types=None, receive=None):
    # Логирование в консоль + файл Logs
    file = 'Logs.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'ID_User: [{time.strftime("%H: %M: %S")}] [{message.from_user.id}] Name: [{message.from_user.first_name} {message.from_user.last_name}]: [{message.text}]\n')
        print(
            f'ID_User: {time.strftime("%H: %M: %S")} {message.from_user.id} Name: {message.from_user.first_name} {message.from_user.last_name}: {message.text} ')


    if message.text == 'Info':
        bot.send_message(message.chat.id, 'Приветсвтую тебя!!\n'
                                          'Bot created for educational purposes. Author Oleg Tkachev 🥸 11/2022.')
        bot.send_message(message.chat.id, 'Мои возможность на сегодя:\n'
                                          '[Info] ==> Инфо меню\n'
                                          '[Погода] ==> Погода в городе\n'
                                          '[Cats] ==> Веселые котики\n'
                                          '[Geme] ==> Игра угадай число\n'
                                          # '[Юмор] ==> Веселые анекдоты\n'
                                          '[Калькулятор] ==> No comments  😏)\n')

    elif message.text == 'Game':
        global count
        count = 5
        r = bot.send_message(message.chat.id, 'Приветсвтую тебя!!\n'
                                              'Давай-ка поиграем, в угадайку чисел !')
        bot.send_message(message.chat.id, '"УГАДАЙ ЦИФРУ"!\n Количество попыток: [5]')
        bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 10 !')
        bot.register_next_step_handler(r, game_unknown_number)

    elif message.text == 'Погода':
        s = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, s.text)

    elif message.text == 'Cats':
        m = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, m)

    elif message.text == 'Калькулятор':
        z = bot.send_message(message.chat.id, 'Давай что-нибудь посчитаем 😏 ')
        bot.register_next_step_handler(z, Calculate)

    elif message.text.lower() == 'file':
        data = open('Logs.txt', encoding='utf-8')
        bot.send_document(message.chat.id, data)
        data.close()


bot.infinity_polling()
