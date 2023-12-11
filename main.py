import os
import json
from PIL import Image, ImageDraw, ImageFont

from SendMessage import SendMessageEmail

DIR = os.path.dirname(__file__)

# Загрузка данных из JSON файла
json_file_path = ('%s/название_файла.json' % DIR)

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Папка с изображениями
image_folder = ('%s/image' % DIR)

# Папка для временных файлов (изображений с фамилией)
temp_folder = ('%s/tmp_dic' % DIR)
os.makedirs(temp_folder, exist_ok=True)


# Функция для вставки фамилии в изображение
def insert_text_into_image(image_path, name, output_path):
    img = Image.open(image_path)

    font = ImageFont.truetype(("%s/ttf/ALS_Regular.otf" % DIR), 120)  # Шрифт меняется по вашему желанию
    drawer = ImageDraw.Draw(img)

    text_bbox = drawer.textbbox((0, 0), name, font=font)
    x_coordinate = (img.width - text_bbox[2]) // 2

    drawer.text((x_coordinate, 1390), name, font=font, fill='black')
    img.save(output_path)


# Функция для отправки электронной почты с изображением
def send_email(receiver_email, subject, body, image_path):
    sending_message_email = SendMessageEmail()

    sending_message_email.setting('smtp.gmail.com', 465, "ваша_почта@gmail.com", 'ваш_пароль')

    sending_message_email.whom(receiver_email)
    sending_message_email.topic(subject)
    sending_message_email.addImage(image_path, 'PNG')
    sending_message_email.addText(body)

    sending_message_email.send()
    sending_message_email.quit()


# Обработка данных и выполнение задач
for fio, info in data.items():
    for id_value in info['id']:
        image_path = os.path.join(image_folder, f'mc_{id_value}.png')
        temp_image_path = os.path.join(temp_folder, f'{fio}_mc_{id_value}.png')

        # Вставка фамилии в изображение
        insert_text_into_image(image_path, fio, temp_image_path)

        # Отправка электронной почты с изображением
        send_email(info['email'], 'Тема письма', 'Текст письма', temp_image_path)

        # Удаление временного изображения
        os.remove(temp_image_path)

print('Задачи выполнены успешно.')
