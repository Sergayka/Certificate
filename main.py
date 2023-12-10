# import os
# import smtplib
# from email.mime.audio import MIMEAudio
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from PIL import Image, ImageDraw, ImageFont
#
# DIR = "D://GitHub/Certificate"
# # DIR = os.path.dirname(__file__)
# print(DIR)
#
#
# class SendMessageEmail:
#     def setting(self, server, port, login, password):
#         self.server = smtplib.SMTP_SSL(server, port)  # Создаем объект SMTP
#         self.server.login(login, password)  # Получаем доступ
#         self.message = MIMEMultipart()  # Создаем сообщение
#         self.message['From'] = login  # Адресат
#
#     def tls(self):
#         self.server.starttls()  # Начинаем шифрованный обмен по TLS
#
#     def recipient(self, email):
#         self.message['To'] = email  # Получатель
#
#     def topic(self, string):
#         self.message['Subject'] = string  # Тема сообщения
#
#     def add_text(self, text):
#         self.message.attach(MIMEText(text, 'plain'))
#
#     def add_html(self, html, encoding):
#         self.message.attach(MIMEText(html, 'html', encoding))  # Добавляем в сообщение HTML-фрагмент
#
#     def add_image(self, path, file_type):
#         path = os.path.abspath(path)
#         file_name = path.split('\\')[-1]
#
#         with open(path, 'rb') as file:
#             file = MIMEImage(file.read(), file_type)
#             file.add_header('Content-Disposition', 'attachment', filename=file_name)  # Добавляем заголовки
#
#         self.message.attach(file)
#
#     def send(self):
#         self.server.send_message(self.message)  # Отправляем сообщение
#
#     def debug(self, boolean):
#         self.server.set_debuglevel(boolean)
#
#     def quit(self):
#         self.server.quit()
#
#
# def get_certificate(name: str, type_mc: int) -> str:
#     printing_image = Image.open('%s/image/clear.png' % DIR)
#     print(printing_image)
#     font = ImageFont.truetype("ttf/ALS_Regular.otf", 90)
#     drawer = ImageDraw.Draw(printing_image)
#     text_bbox = drawer.textbbox((0, 0), name, font=font)
#     x_coordinate = (printing_image.width - text_bbox[2]) // 2
#     drawer.text((x_coordinate, 987), name, font=font, fill='black')
#     printing_image.save(f'{DIR}/{name}.png')
#
#     # if type_mc == 1:
#     #     sending_image = Image.open(f'{DIR}/image/mc_web.png')
#     # elif type_mc == 2:
#     #     sending_image = Image.open(f'{DIR}/image/mc_game.png')
#     #
#     # font = ImageFont.truetype("ttf/ALS_Regular.otf", 120)  # Font can be changed
#     # drawer = ImageDraw.Draw(sending_image)
#     #
#     # text_bbox = drawer.textbbox((0, 0), name, font=font)
#     # x_coordinate = (sending_image.width - text_bbox[2]) // 2
#     #
#     # drawer.text((x_coordinate, 1390), name, font=font, fill='black')
#     #
#     # sending_image.save(f"{DIR}/{name}.png")
#
#     return f"{name}.png"
#
#
# def send_certificate(name: str, mail: str, type_mc: int) -> None:
#     # print(f'{DIR}/image/mc_web.png')
#     # sending_image = Image.open(f'{DIR}/image/mc_web.png')
#     # if type_mc == 1:
#     #     sending_image = Image.open(f'{DIR}/image/mc_web.png')
#     # elif type_mc == 2:
#     #     sending_image = Image.open(f'{DIR}/image/mc_game.png')
#     # print(sending_image)
#     # font = ImageFont.truetype("ttf/ALS_Regular.otf", 120)  # Font can be changed
#     # drawer = ImageDraw.Draw(sending_image)
#     img = DIR + '/' + get_certificate(name, type_mc)
#
#     # text_bbox = drawer.textbbox((0, 0), name, font=font)
#     # x_coordinate = (sending_image.width - text_bbox[2]) // 2
#     #
#     # drawer.text((x_coordinate, 1390), name, font=font, fill='black')
#     #
#     # sending_image.save(f'{DIR}/{name}.png')
#
#     sending_message_email = SendMessageEmail()
#     sending_message_email.setting('smtp.gmail.com', 465, "iuk2.master.class@gmail.com", 'jmni xucl gvpy ixkp')
#     sending_message_email.recipient(mail)
#     sending_message_email.topic("Свидетельство")
#     sending_message_email.add_image(img, 'PNG')
#     sending_message_email.add_text(
#         'Поздравляем с успешным прохождением мастер-класса от кафедры ИУК2 "Инфорамционные системы и сети"')
#     sending_message_email.send()
#     sending_message_email.quit()
#
#     # os.remove(f'{name}.png')
#
#     # get_certificate(name)
#
#
# def main():
#     #     while True:
#     for _ in range(2):
#         # try:
#         name = input("Enter name: ")
#         # name = 'Филатов Сергей'
#         # type_mc = 3
#         mail = input("mail: ")
#         type_mc = int(input("MC: "))
#         send_certificate(name, mail, type_mc)  # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=3508x2480 at 0x28F9F081E90>
#         # os.remove(f'{name}.png')
#         # Se(name)
#         # get_certificate(name) #<PIL.PngImagePlugin.PngImageFile image mode=RGB size=2480x1748 at 0x22E4C6CA850>
#         print('ok')
#
#         # except Exception as e:
#         #     print(f'error: {e}' )
#
#
# # except Exception as e:
# #     print('error: {}'.format(str(e)))
#
#
# if __name__ == '__main__':
#     main()


import os
import smtplib
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageDraw, ImageFont

DIR = "D://GitHub/Certificate"
# DIR = os.path.dirname(__file__)


class SendMessageEmail:
    def setting(self, server, port, login, password):
        self.server = smtplib.SMTP_SSL(server, port)  # Создаем объект SMTP
        self.server.login(login, password)  # Получаем доступ
        self.message = MIMEMultipart()  # Создаем сообщение
        self.message['From'] = login  # Адресат

    def tls(self):
        self.server.starttls()  # Начинаем шифрованный обмен по TLS

    def whom(self, email):
        self.message['To'] = email  # Получатель

    def topic(self, string):
        self.message['Subject'] = string  # Тема сообщения

    def addText(self, text):
        self.message.attach(MIMEText(text, 'plain'))

    def addHtml(self, html, encoding):
        self.message.attach(MIMEText(html, 'html', encoding))  # Добавляем в сообщение HTML-фрагмент

    def addImage(self, path, file_type):
        path = os.path.abspath(path)
        file_name = path.split('\\')[-1]
        with open(path, 'rb') as file:
            file = MIMEImage(file.read(), file_type)
            file.add_header('Content-Disposition', 'attachment', filename=file_name)  # Добавляем заголовки
        self.message.attach(file)

    def addAudio(self, path, file_type):
        path = os.path.abspath(path)
        file_name = path.split('\\')[-1]
        with open(path, 'rb') as file:
            file = MIMEAudio(file.read(), file_type)
            file.add_header('Content-Disposition', 'attachment', filename=file_name)  # Добавляем заголовки
        self.message.attach(file)

    def send(self):
        self.server.send_message(self.message)  # Отправляем сообщение

    def debug(self, boolean):
        self.server.set_debuglevel(boolean)

    def quit(self):
        self.server.quit()


def get_certificate(name, type_mc):
    if type_mc == 1:
        # image = Image.open('%s/image/mc_web.png' % DIR)
        image = Image.open(f'{DIR}/image/mc_web.png')
    elif type_mc == 2:
        image = Image.open('%s/image/mc_game.png' % DIR)

    print(f'{DIR}/image/mc_web.png')

    font = ImageFont.truetype(f"{DIR}/ttf/ALS_Regular", 65)  # Font can be changed
    drawer = ImageDraw.Draw(image)

    text_bbox = drawer.textbbox((0, 0), name, font=font)
    x_coordinate = (image.width - text_bbox[2]) // 2

    drawer.text((x_coordinate, 1390), name, font=font, fill='black')
    image.save(f"{DIR}/{name}.png")
    # print(DIR + '/' + name)
    return f"{name}.png"


def send_certificate(name, mail, type_mc):
    img = DIR + '/' + get_certificate(name, type_mc)
    print(DIR + '/' + get_certificate(name, type_mc))
    sending_message_email = SendMessageEmail()
    sending_message_email.setting('smtp.gmail.com', 465, "iuk2.master.class@gmail.com", 'jmni xucl gvpy ixkp')
    sending_message_email.whom(mail)
    sending_message_email.topic("Свидетельство")
    sending_message_email.addImage(img, 'PNG')
    sending_message_email.addText(
        'Поздравляем с успешным прохождением мастер-класса от кафедры ИУК2 "Инфорамционные системы и сети"')
    sending_message_email.send()
    sending_message_email.quit()


# def main():
#     while True:
#         try:
#             name = input("Enter name: ")
#             mail = input("mail: ")
#             type_mc = int(input("MC: "))
#             send_certificate(name, mail, type_mc)
#             print('ok')
#
#         except Exception as e:
#             print('error: {}'.format(str(e)))
#

# if __name__ == '__main__':
#     main()


name = input("Enter name: ")
mail = input("mail: ")
type_mc = int(input("MC: "))
send_certificate(name, mail, type_mc)
print('ok')