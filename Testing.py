import pandas as pd
import json

# Загрузка данных из XLSX файла
xlsx_file_path = 'название_файла.xlsx'
df = pd.read_excel(xlsx_file_path)

# Загрузка данных из JSON файла
json_file_path = 'название_файла.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Получение фамилий из столбца D в XLSX файле
xlsx_surnames = df['ФИО'].tolist()

# Проверка присутствия фамилий из JSON файла в XLSX файле
present_surnames = [surname for surname in json_data.keys() if surname in xlsx_surnames]
absent_surnames = [surname for surname in json_data.keys() if surname not in xlsx_surnames]

# Вывод результатов
print("Присутствующие фамилии в XLSX файле:", present_surnames)
print("Отсутствующие фамилии в XLSX файле:", absent_surnames)
