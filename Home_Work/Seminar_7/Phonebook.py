

def read_CSV():
    file = 'Phonebook.csv'
    with open(file, 'r', encoding='utf-8') as data:
        # contackt = data.read()
        print("Контакты:\n", data.read())


def writing_scv (information):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Имя: {information[0] }; Фамилия: { information[1]}; Телефон: { information[2] }; Описание: { information[3] }\n')

print(read_CSV())
