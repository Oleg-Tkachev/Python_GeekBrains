# Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

# Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import requests
from telebot import types
import telebot
import time

bot = telebot.TeleBot("5932647150:AAGU1GllNxW4lPWnct9ynbxCEg3FWlckc7c", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('Info')
itembtn2 = types.KeyboardButton('Game')
itembtn3 = types.KeyboardButton('Погода')
itembtn4 = types.KeyboardButton('Cats')
itembtn5 = types.KeyboardButton('Юмор')
itembtn6 = types.KeyboardButton('Калькулятор')
itembtn7 = types.KeyboardButton('file')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)


@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Добрый человек :) ' + message.from_user.first_name, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def hello_user(message, content_types=None, receive=None):
    # Логирование в консоль + файл Logs
    file = 'Logs.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'ID_User: [{message.from_user.id}] Name: [{message.from_user.first_name} {message.from_user.last_name}]: [{message.text}]\n')
        print(
            f'ID_User: {message.from_user.id} Name: {message.from_user.first_name} {message.from_user.last_name}: {message.text} ')


@bot.message_handler(commands=['text'])
def send_welcome(message):
    if message.text == 'Info':
        bot.send_message(message.chat.id, 'Приветсвтую тебя!!\n'
                                          'Bot created for educational purposes. Avtor Oleg Tkachev  11/2022.')
        bot.send_message(message.chat.id, 'Мои возможность на сегодя:\n'
                                          '[Info] ==> Информация возможностей\n'
                                          '[Погода] ==> Погода в городе\n'
                                          '[Cats] ==> Веселые котики\n'
                                          '[Geme] ==> Игра угадай число\n'
                                          '[Юмор] ==> Веселые анекдоты\n'
                                          '[Калькулятор] ==> No comments)\n')

    elif message.text == 'Game':
        bot.send_message(message.chat.id, 'Приветсвтую тебя!!\n'
                                          'Давай-ка поиграем, в угадайку чисел!')

    elif message.text == 'Погода':
        s = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, s.text)

    elif message.text == 'Cats':
        m = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, m)

    elif message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Приветсвтую тебя!!')

    else:
        message.text.lower() == 'файл'
        data = open('user_message.txt', encoding='utf-8')
        bot.send_document(message.chat.id, data)
        data.close()


bot.infinity_polling()


