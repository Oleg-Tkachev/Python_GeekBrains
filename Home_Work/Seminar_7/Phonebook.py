

def read_CSV():
    file = 'Phonebook.csv'
    with open(file, 'r', encoding='utf-8') as data:
        print('Контакты:\n', data.read())


def writing_scv(information):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Имя: [{information[0] }]; Фамилия: [{ information[1]}]; Телефон: [+7{ information[2] }]; Описание: [{ information[3] }]\n')


def export_scv():
    file = 'Phonebook.csv'
    export_scv = 'Contack.html'
    with open(file, 'r', encoding='utf-8') as data:
        contakts = data.read()
        with open(export_scv, 'w', encoding='utf-8') as data:
            con = data.write(contakts)
            print('Файл сохранен в формате HTML')


