import Interface
import Phonebook


def select_menu():
    print('Выберите действие:\n'
          '1 - Записать контакт\n'
          '2 - Просмотр контактов\n'
          '3 - Экспорт контактов в файл HTML')
    select = int(input())
    if select == 1:
        Phonebook.writing_scv(Interface.creat_information())
    if select == 2:
        Phonebook.read_CSV()
    if select == 3:
        Phonebook.export_scv()
    else:
        if select != 1 or select != 2 or select != 3:
            print('Некорректный ввод')


