
import Interface

information = []
def creat_file_CSV():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия; Имя; Номер телефона; Описание\n')

def writing_scv (information=None):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{information[0]};{information[1]};{information[2]};{information[3]}\n')
