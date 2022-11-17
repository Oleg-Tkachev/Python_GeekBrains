
information = []

def creat_information():

    first_name = input('Введите имя: ')
    information.append(first_name)

    last_name = input('Введите фамилию: ')
    information.append(last_name)

    phone_number = None
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона +7: ')
            if len(phone_number) != 10:
                print('В номере телефона должно быть 10 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Некорректный ввод')
    information.append(phone_number)
    remark = input('Добавьте описание: ')
    information.append(remark)
    return information


