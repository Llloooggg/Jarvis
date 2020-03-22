import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail():
    mail_sender = '' #отправитель
    mail_receiver = '' #адресат
    username = '' #имя пользователя
    password = '' #пароль от почты
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Формируем тело письма
    subject = u'Тестовый email от '
    body = u'Отправка письма на Питтоне '
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # Отпавляем письмо
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()
