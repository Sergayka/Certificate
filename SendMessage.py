import os
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


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

    def send(self):
        self.server.send_message(self.message)  # Отправляем сообщение

    def debug(self, boolean):
        self.server.set_debuglevel(boolean)

    def quit(self):
        self.server.quit()
