import pandas as pd
import json

# Загрузка файла xlsx
file_path = 'mc.xlsx'
df = pd.read_excel(file_path)

# Создание пустого словаря для хранения данных
data_dict = {}

# Итерация по строкам датафрейма
for index, row in df.iterrows():
    fio = " ".join(row['ФИО'].split()[:2]).title()#row['ФИО'] #" ".join(row[3].split()[:2])
    email = row['Активная почта']
    master_class = row['Мастер-класс']

    # Определение id в зависимости от значения столбца 'Мастер-Класс'
    if master_class == 'Создай игру на Python':
        id_value = 1
    elif master_class == 'Создай веб-приложение "Записная книжка"':
        id_value = 2
    else:
        id_value = None  # Здесь вы можете обработать другие значения 'Мастер-Класс'

    # Добавление данных в словарь
    if id_value is not None:
        if fio not in data_dict:
            data_dict[fio] = {'email': email, 'master_classes': []}

        # Проверка, чтобы избежать дублирования мастер-классов
        if id_value not in data_dict[fio]['master_classes']:
            data_dict[fio]['master_classes'].append(id_value)

# Преобразование данных в нужный формат для JSON
result_data = {}
for fio, info in data_dict.items():
    result_data[fio] = {'email': info['email'], 'id': info['master_classes']}

# Запись данных в JSON файл
json_file_path = 'output1.json'
with open(json_file_path, 'w') as json_file:
    json.dump(result_data, json_file, ensure_ascii=False, indent=4)

print(f'Данные успешно записаны в файл: {json_file_path}')
