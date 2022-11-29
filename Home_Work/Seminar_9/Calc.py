from __future__ import division
from operator import truediv, mul, add, sub
import multiplication as multiplication


operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}


def Calc_bot(message):
    if message.isdigit():
        return float(message)
    for i in operators.keys():
        left, operator, right = s.partition(i)
        if operator in operators:
            return operators[operator](Calc_bot(left), Calc_bot(right))

    calc = input(f'Введите математическое выражение: \n')
    print(f'Результат: {str(Calc_bot(calc))}')


Calc_bot(message)

