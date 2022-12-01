from Main import bot


def Calculate(message):
    print("33333333333333333")
    if '+' in message.text or '*' in message.text or '/' in message.text or '-' in message.text:
        calculate = str(eval(str(message.text)))
        bot.send_message(message.chat.id, f'{calculate}')
    else:
        bot.send_message(message.chat.id, 'Не в моих силах такое вычислить')






# Надо добить код!
# operators = {
#     '+': addition,
#     '-': subtraction,
#     '*': multiplication,
#     '/': division
# }
#
#
# def Calc_bot(message):
#     if message.isdigit():
#         return float(message)
#     for i in operators.keys():
#         left, operator, right = s.partition(i)
#         if operator in operators:
#             return operators[operator](Calc_bot(left), Calc_bot(right))
#
#     calc = input(f'Введите математическое выражение: \n')
#     print(f'Результат: {str(Calc_bot(calc))}')