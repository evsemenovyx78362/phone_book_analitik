import csv

# Данные для телефонного справочника
contacts = [
    {"Имя": "Иван", "Фамилия": "Иванов", "Телефон": "+7 123 456-78-90"},
    {"Имя": "Мария", "Фамилия": "Петрова", "Телефон": "+7 987 654-32-10"},
    {"Имя": "Сергей", "Фамилия": "Сергеев", "Телефон": "+7 456 789-12-34"},
]

# Название файла CSV
filename = 'phone_book.csv'

# Запись данных в CSV файл
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Имя", "Фамилия", "Телефон"])
    
    # Записываем заголовок
    writer.writeheader()
    
    # Записываем строки данных
    writer.writerows(contacts)

print(f"Телефонный справочник сохранен в файл '{filename}'")