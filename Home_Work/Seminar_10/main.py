# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
#
# Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.


from telebot import types
import telebot
import time

bot = telebot.TeleBot("5932647150:AAGU1GllNxW4lPWnct9ynbxCEg3FWlckc7c", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn_1 = types.KeyboardButton('Меню')
itembtn_2 = types.KeyboardButton('Заказ')
itembtn_3 = types.KeyboardButton('Роллы')
itembtn_4 = types.KeyboardButton('Паста')
itembtn_5 = types.KeyboardButton('Пицца')
itembtn_6 = types.KeyboardButton('Кофе')
markup.add(itembtn_1, itembtn_2, itembtn_3, itembtn_4, itembtn_5, itembtn_6)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, message.from_user.first_name + ", Привет, Ты голоден ? заказывай !' ", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def prog_bot(message, content_types=None, receive=None):
    # Логирование в консоль + файл Logs
    file = 'Logs.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'ID_User: [{time.strftime("%H: %M: %S")}] [{message.from_user.id}] Name: [{message.from_user.first_name} {message.from_user.last_name}]: [{message.text}]\n')
        print(
            f'ID_User: {time.strftime("%H: %M: %S")} {message.from_user.id} Name: {message.from_user.first_name} {message.from_user.last_name}: {message.text} ')

    if message.text == 'Меню':
        bot.send_message(message.chat.id, 'Меню на сегодня:\n'
                                          '[Роллы] ==> Калифорния \n'
                                          '[Паста] ==> Паста с сыром\n'
                                          '[Пицца] ==> С грибами\n'
                                          '[Кофе] ==> Капучино \n')

    elif message.text == 'Роллы':
        bot.send_message(message.chat.id, 'Роллы "Калифорния" в заказ добавлены, \n')
        order = 'order.txt'
        with open(order, 'a', encoding='utf-8') as data:
            data.write(f'[ Роллы "Калифорния" ]\n')

    elif message.text == 'Паста':
        order = 'order.txt'
        bot.send_message(message.chat.id, 'Паста с сыром в заказ добавлена\n')
        with open(order, 'a', encoding='utf-8') as data:
            data.write(f'[ Паста с сыром ]\n')

    elif message.text == 'Пицца':
        order = 'order.txt'
        bot.send_message(message.chat.id, 'Пицца c грибами в заказ добавлена \n')
        with open(order, 'a', encoding='utf-8') as data:
            data.write(f'[ Пицца С грибами ] \n')

    elif message.text == 'Кофе':
        order = 'order.txt'
        bot.send_message(message.chat.id, 'Капучино, в заказ добавлено\n')
        with open(order, 'a', encoding='utf-8') as data:
            data.write(f'[ Капучино ] \n')

    elif message.text == 'Заказ':
        order = 'order.txt'

        with open(order, 'r', encoding='utf-8') as data:
            s = data.read()
            print(s)
            bot.send_message(message.chat.id, message.from_user.first_name + ", Ваш заказ: \n")
            bot.send_message(message.chat.id, s)


bot.infinity_polling()
