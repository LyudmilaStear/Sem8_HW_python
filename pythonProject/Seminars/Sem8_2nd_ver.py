"""import os

phonebook = []

def display_menu():
    print("\nТелефонный справочник:")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Найти запись")
    print("4. Изменить запись")
    print("5. Удалить запись")
    print("6. Сохранить в файл")
    print("7. Загрузить из файла")
    print("8. Выход")

def display_contacts():
    if not phonebook:
        print("Телефонный справочник пуст.")
    else:
        print("\nЗаписи в телефонном справочнике:")
        for contact in phonebook:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")

def add_contact():
    contact = {}
    contact['Фамилия'] = input("Введите фамилию: ")
    contact['Имя'] = input("Введите имя: ")
    contact['Отчество'] = input("Введите отчество: ")
    contact['Телефон'] = input("Введите номер телефона: ")
    phonebook.append(contact)
    print("Запись добавлена.")

def find_contact():
    search_term = input("Введите имя или фамилию для поиска: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        print("\nНайденные записи:")
        for contact in found_contacts:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")
    else:
        print("Записи не найдены.")

def edit_contact():
    search_term = input("Введите имя или фамилию для поиска записи, которую вы хотите изменить: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        display_contacts()
        choice = int(input("Введите номер записи, которую вы хотите изменить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            print(f"\nРедактирование записи: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")
            contact['Фамилия'] = input("Введите новую фамилию: ")
            contact['Имя'] = input("Введите новое имя: ")
            contact['Отчество'] = input("Введите новое отчество: ")
            contact['Телефон'] = input("Введите новый номер телефона: ")
            print("Запись изменена.")
        else:
            print("Некорректный выбор.")
    else:
        print("Записи не найдены.")

def delete_contact():
    search_term = input("Введите имя или фамилию для поиска записи, которую вы хотите удалить: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        display_contacts()
        choice = int(input("Введите номер записи, которую вы хотите удалить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            phonebook.remove(contact)
            print("Запись удалена.")
        else:
            print("Некорректный выбор.")
    else:
        print("Записи не найдены.")

def save_to_file():
    filename = input("Введите имя файла для сохранения: ")
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}\n")
    print(f"Данные сохранены в файл {filename}.")

def load_from_file():
    filename = input("Введите имя файла для загрузки: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            phonebook.clear()
            for line in lines:
                parts = line.split(':')
                name_parts = parts[0].split()
                contact = {
                    'Фамилия': name_parts[0],
                    'Имя': name_parts[1],
                    'Отчество': name_parts[2],
                    'Телефон': parts[1].strip()
                }
                phonebook.append(contact)
        print(f"Данные загружены из файла {filename}.")
    else:
        print("Файл не найден.")

def main():
    while True:
        display_menu()
        choice = int(input("Выберите операцию (от 1 до 8): "))
        if choice == 1:
            display_contacts()
        elif choice == 2:
            add_contact()
        elif choice == 3:
            find_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            save_to_file()
        elif choice == 7:
            load_from_file()
        elif choice == 8:
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 8.")

if __name__ == "__main__":
    main()
    """

'''
Задача №49 - с семинара:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные;
2. Программа должна сохранять данные в текстовом файле;
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например, имя или фамилию
человека);
4. Использование функций. Ваша программа не должна быть линейной.

Домашнее задание:
Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, 
которую необходимо перенести из одного файла в другой.
Формат сдачи: ссылка на пулл в свой репозиторий.
'''

from os.path import exists
from csv import DictReader, DictWriter

def get_info():
    first_name = "Иван"
    last_name = "Иванов"
    phone_number = "89999887766"
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def create_file_copies(file_name_copies):
    with open(file_name_copies, 'w', encoding='utf-8') as data:
        data.write()

def get_copy_line():
    line_index = int(input("Введите номер строки для копирования: ")) - 1
    return line_index

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'
file_name_copies = 'copies.csv'

def copy_file_line(file_name, file_name_copies, line_index):
    res_line = []
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = data.read()
        res = list(f_reader.split("\n"))
        if line_index < len(res):
            res_line.append(res[line_index])
        else:
            print('Такой строки в файле нет!\n')

    with open(file_name_copies, 'a', encoding='utf-8') as data_1:
        data_1.seek(2)
        data_1.write("\n")
        data_1.writelines("\n".join(res_line))

    if line_index < len(res):
        print(f'Строка № {line_index + 1} скопирована.\n')

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_file_line(file_name, file_name_copies, get_copy_line())

main()