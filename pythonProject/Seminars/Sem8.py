"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue


    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(first_name) < 2:
                raise NameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue


    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue

        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже существует!")
            return
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'
new_file = 'new_phone.csv'

# def find_by_attribute(file_name: str, option: bool):
#     c = input("Введите 1 для поиска по фамилии, 2 для поиска по имени")
#     opt = 0
#     if c == '1':
#         opt = 0
#     elif c == '2':
#         opt = 1
#
#     attr = input("Введите имя/фамилию для поиска")
#     with open(file_name, 'r', encoding='utf-8') as f:
#         data = f.readlines()
#         data = list(filter(lambda x: x.split(', ')[opt] == attr, data))
#         print(list(zip(range(1, len(data) + 1), data)))
#         if option:
#             id = input("Введите id нужного пользователя для изменения данных: ")
#         else:
#             id = input("Введите id нужного пользователя: ")
#         return data[int(id) - 1]

def get_copy_line():
    line_index = int(input("Введите номер строки для копирования: ")) - 1
    return line_index

def copy_file_line(file_name, new_file, line_number):
    res_line = []
    with open(file_name, 'r', encoding='utf-8') as file1:
        f_reader = file1.read()
        res = list(f_reader.split("\n"))
        if line_number < len(res):
            res_line.append(res[line_number])
        else:
            print('Такой строки в файле нет!\n')

    with open(new_file, 'a', encoding='utf-8') as data_1:
        data_1.seek(2)
        data_1.write("\n")
        data_1.writelines("\n".join(res_line))

    if line_number < len(res):
        print(f'Строка № {line_number + 1} скопирована.\n')

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file("\n".join(file_name, get_info()))
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        # elif command == 'f':
        #     if not exists(file_name):
        #         print("Файл отсутствует. Создайте его")
        #         continue
        #     print(*find_by_attribute(file_name, option))
        elif command == 'c':
            copy_file_line(file_name, new_file, get_copy_line())


main()




#copy_line('phone.csv', 'new_phone.csv', 3)


# def save_to_file():
#     filename = 'new_phone.csv'
#     with open(filename, 'w') as file:
#         for line in 'phone.csv':
#             obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
#             file.write(f"{"Имя": lst[0]}, {"Фамилия": lst[1]}, {"Телефон": lst[2]}")
#             #{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}
#             #obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
#     print(f"Данные сохранены в файл new_phone.csv.")
#
# save_to_file()
