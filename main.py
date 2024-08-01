import csv

# Имя файла CSV
filename = 'phone_book.csv'

def load_contacts(filename):
    """Загрузить контакты из CSV файла."""
    contacts = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(filename, contacts):
    """Сохранить контакты в CSV файл."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Имя", "Фамилия", "Телефон"])
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    """Добавить новый контакт."""
    имя = input("Введите имя: ")
    фамилия = input("Введите фамилию: ")
    телефон = input("Введите телефон: ")
    contacts.append({"Имя": имя, "Фамилия": фамилия, "Телефон": телефон})

def update_contact(contacts):
    """Изменить существующий контакт."""
    имя = input("Введите имя контакта для изменения: ")
    фамилия = input("Введите фамилию контакта для изменения: ")

    for contact in contacts:
        if contact["Имя"] == имя and contact["Фамилия"] == фамилия:
            print("Контакт найден.")
            новый_телефон = input("Введите новый телефон: ")
            contact["Телефон"] = новый_телефон
            return

    print("Контакт не найден.")

def delete_contact(contacts):
    """Удалить контакт."""
    имя = input("Введите имя контакта для удаления: ")
    фамилия = input("Введите фамилию контакта для удаления: ")

    for i, contact in enumerate(contacts):
        if contact["Имя"] == имя and contact["Фамилия"] == фамилия:
            del contacts[i]
            print("Контакт удален.")
            return

    print("Контакт не найден.")

def display_contacts(contacts):
    """Показать все контакты."""
    if contacts:
        for contact in contacts:
            print(f"{contact['Имя']} {contact['Фамилия']}: {contact['Телефон']}")
    else:
        print("Телефонный справочник пуст.")

def main():
    contacts = load_contacts(filename)

    while True:
        print("\nТелефонный справочник:")
        print("1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print("Изменения сохранены. Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()