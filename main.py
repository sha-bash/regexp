import re
import csv
from pprint import pprint

# Функция для корректировки ФИО
def correct_names(contact):
    full_name = ' '.join(contact[:3]).split()
    return full_name + contact[3:]

# Функция для форматирования номеров телефонов
def format_phone_number(phone):
    phone_pattern = re.compile(r'(d{1,2})?D*(d{3})D*(d{3})D*(d{2})D*(d{2})(D*(d+))?')
    formatted_phone = phone_pattern.sub(r'+7(2)3-4-5 7', phone).strip()
    return formatted_phone.replace('  ', ' доб.')

# Чтение данных из файла
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Обработка данных
for i, contact in enumerate(contacts_list):
    contacts_list[i] = correct_names(contact)
    contacts_list[i][5] = format_phone_number(contact[5])

# Удаление дубликатов
unique_contacts = {}
for contact in contacts_list:
    key = (contact[0], contact[1])  # Фамилия и имя как ключ
    if key in unique_contacts:
        for j in range(len(contact)):
            if contact[j]:
                unique_contacts[key][j] = contact[j]
    else:
        unique_contacts[key] = contact

# Подготовка данных к записи
final_contacts_list = list(unique_contacts.values())

# Запись данных в новый файл
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)

pprint(final_contacts_list)
