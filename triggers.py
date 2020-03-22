import datetime
import email
import imaplib
import time


def test_trigger(var, tg_id):
    time.sleep(int(var))


# Будильник
# Формат строки (год месяц день час минута секунда)
# Config_time='2020#3#22#15#20#0'
def alarm_clock(config_time, tg_id):
    config_list = config_time.split('#')
    dt = datetime.datetime(int(config_list[0]), int(config_list[1]), int(config_list[2]), int(config_list[3]),
                           int(config_list[4]),
                           int(config_list[5]))
    diff = (dt - datetime.datetime.now()).total_seconds()
    try:
        time.sleep(diff)
    except:
        print('Нельзя поставить будильник в прошлое')
    return


# проверка почты на новое письмо gmail
# Нужно включить https://myaccount.google.com/lesssecureapps и https://mail.google.com/mail/u/2/#settings/fwdandpop
# Формат строки (логин#пароль)
# check_mail_config='login@gmail.com Password123'
def check_email(check_mail_config, tg_id):
    mail_config_list = check_mail_config.split('#')
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(mail_config_list[0], mail_config_list[1])
    mail.list()
    count_Email_Start = (mail.select("inbox")[1][0]).decode('utf-8')
    while True:
        mail.list()
        count_Email_Current = (mail.select("inbox")[1][0]).decode('utf-8')
        if count_Email_Current > count_Email_Start:
            result, data = mail.search(None, "ALL")
            ids = data[0]  # Получаем сроку номеров писем
            id_list = ids.split()  # Разделяем ID писем
            latest_email_id = id_list[-1]  # Берем последний ID
            result, data = mail.fetch(latest_email_id, "(RFC822)")  # Получаем тело письма (RFC822) для данного ID
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            email_message_From = email_message['From']
            email_message_From = email_message_From[email_message_From.index('<'):email_message_From.index('>')]
            email_message_From = email_message_From[1:]
            return
            # count_Email_Start = count_Email_Current
        time.sleep(15)  # частота проверки нового письма
