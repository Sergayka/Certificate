import os
import smtplib
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image, ImageDraw, ImageFont



# DIR = "C://Users/Armine/Desktop/certificates"
DIR = "D://GitHub/Certificate"


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
        printing_image = Image.open('%s/image/mc_web.png' % DIR)
    elif type_mc == 2:
        printing_image = Image.open('%s/image/mc_web.png' % DIR)

    font = ImageFont.truetype(f"{DIR}/ttf/ALS_Regular", 65)  # Font can be changed
    drawer = ImageDraw.Draw(image)
    drawer.text((700, 1500), name, font=font, fill='black')
    image.save(f"{DIR}/{name}.png")
    return f"{name}.png"


def send_certificate(name, mail, type_mc):
    img = DIR + '/' + get_certificate(name, type_mc)
    sending_message_email = SendMessageEmail()
    sending_message_email.setting('smtp.gmail.com', 465, "iuk2.master.class@gmail.com", 'jmni xucl gvpy ixkp')
    sending_message_email.whom(mail)
    sending_message_email.topic("Свидетельство")
    sending_message_email.addImage(img, 'PNG')
    sending_message_email.addText(
        'Поздравляем с успешным прохождением мастер-класса от кафедры ИУК2 "Инфорамционные системы и сети"')
    sending_message_email.send()
    sending_message_email.quit()


# while True:
#     try:
name = input("Enter name: ")
mail = input("mail: ")
type_mc = int(input("MC: "))
send_certificate(name, mail, type_mc)
print('ok')

    # except Exception as e:
    #     print('error: {}'.format(str(e)))
