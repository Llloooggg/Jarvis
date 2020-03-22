import smtplib
from email.header import Header
from email.mime.text import MIMEText

import telegram


def test_action(var, tg_id):
    print(var)


# Ответ на письмо
# формат строки (логин#пароль#адресат#текст)
# send_mail_config='login@gmail.com#Password123#myfriend@gmail.com#Текст сообщения'
def send_mail(send_mail_config, tg_id):
    send_mail_list = send_mail_config.split('#')
    mail_sender = send_mail_list[0]  # отправитель
    mail_receiver = send_mail_list[2]  # адресат
    username = send_mail_list[0]  # имя пользователя
    password = send_mail_list[1]  # пароль от почты
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Формируем тело письма
    subject = u'J.a.r.v.i.s.'
    body = send_mail_list[3]
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # Отпавляем письмо
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()


def send_message_tg(text, tg_id):
    telegram.send_message(tg_id, text)
