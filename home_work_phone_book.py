def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    '''
    Функция для добавления новой записи в справочник
    :param phonebook: Телефонная книга
    :param last_name: Фамилия
    :param first_name: Имя
    :param middle_name: Отчество
    :param phone_number: Номер телефона
    :return: Телефонная книга с новой записью
    '''
    contact = {
        "last_name": last_name,
        "first_name": first_name,
        "middle_name": middle_name,
        "phone_number": phone_number
    }
    phonebook.append(contact)


def display_contacts(phonebook):
    '''
    Функция для вывода данных из телефонной книги
    :param phonebook: Телефонная книга
    :return: Показывает все записи из телефонной книги
    '''
    for contact in phonebook:
        print(f"Фамилия: {contact['last_name']}")
        print(f"Имя: {contact['first_name']}")
        print(f"Отчество: {contact['middle_name']}")
        print(f"Номер телефона: {contact['phone_number']}")
        print("\t \n")


def export_to_txt(phonebook, filename):
    '''
    Функция для сохранения данных в текстовом файле
    :param phonebook: Телефонная книга
    :param filename: Имя файла ( где сохранять )
    '''
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"Фамилия: {contact['last_name']}\n")
            file.write(f"Имя: {contact['first_name']}\n")
            file.write(f"Отчество: {contact['middle_name']}\n")
            file.write(f"Номер телефона: {contact['phone_number']}\n\n")


def search_contact(phonebook, key, value):
    '''
    Функция для поиска записей по заданной характеристике
    :param phonebook: Телефонная книга
    :param key: Ключ ( искомый параметр )
    :param value: Значение ( искомое значение )
    :return: Вывод искомого
    '''
    found = False
    for contact in phonebook:
        if contact[key] == value:
            print(f"Результаты поиска для {key} ='{value}':")
            print(f"Фамилия: {contact['last_name']}")
            print(f"Имя: {contact['first_name']}")
            print(f"Отчество: {contact['middle_name']}")
            print(f"Номер телефона: {contact['phone_number']}")
            print()
            found = True
    if not found:
        print(f"Запись с {key}='{value}' не найдена.")


def copy_contact_to_file(source_file, dest_file, line_number):
    '''
    Функция для копирования записи из одного файла в другой
    :param source_file: От куда
    :param dest_file: Куда
    :param line_number: Что
    :return: Копия в другом файле
    '''
    with open(source_file, 'r') as source, open(dest_file, 'a') as dest:
        lines = source.readlines()
        if 1 <= line_number <= len(lines):
            dest.write(lines[line_number - 1])
            print(f"Запись {line_number} успешно скопирована из {source_file} в {dest_file}.")
        else:
            print("Недопустимый номер строки.")

def main():
    '''
    Основная функция
    '''
    phonebook = []

    while True:
        print("1. Добавить контакт")
        print("2. Вывести контакты")
        print("3. Сохранить в файл")
        print("4. Поиск по характеристике")
        print("5. Копировать запись из файла")
        print("6. Найти телефон по фамилии")
        print("7. Изменить номер телефона")
        print("8. Удалить запись")
        print("9. Найти абонента по номеру телефона")
        print("10. Добавить абонента в справочник")
        print("11. Закончить работу")

        choice = input("Выберите действие: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            display_contacts(phonebook)
        elif choice == '3':
            filename = input("Введите имя файла для сохранения: ")
            export_to_txt(phonebook, filename)
            print("Данные успешно сохранены в файл.")
        elif choice == '4':
            search_key = input("Введите характеристику для поиска (например, имя или фамилию): ")
            search_value = input(f"Введите {search_key} для поиска: ")
            search_contact(phonebook, search_key, search_value)
        elif choice == '5':
            source_file = input("Введите имя исходного файла: ")
            dest_file = input("Введите имя файла, в который нужно скопировать запись: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_contact_to_file(source_file, dest_file, line_number)
        elif choice == '6':
            last_name = input("Введите фамилию для поиска: ")
            search_contact(phonebook, "last_name", last_name)
        elif choice == '7':
            phone_number = input("Введите номер телефона для изменения: ")
            search_contact(phonebook, "phone_number", phone_number)
            if phone_number in [contact['phone_number'] for contact in phonebook]:
                new_phone_number = input("Введите новый номер телефона: ")
                for contact in phonebook:
                    if contact["phone_number"] == phone_number:
                        contact["phone_number"] = new_phone_number
                        print("Номер телефона успешно изменен.")
                    export_to_txt(phonebook, "contacts.txt")
            else:
                print("Номер телефона не найден.")
        elif choice == '8':
            phone_number = input("Введите номер телефона для удаления: ")
            for contact in phonebook:
                if contact["phone_number"] == phone_number:
                    phonebook.remove(contact)
                    print("Запись успешно удалена.")
                    export_to_txt(phonebook, "2")
                    break
            else:
                print("Номер телефона не найден.")
        elif choice == '9':
            phone_number = input("Введите номер телефона для поиска: ")
            search_contact(phonebook, "phone_number", phone_number)
        elif choice == '10':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '11':
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
