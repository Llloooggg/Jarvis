# Парсер почты
import datetime
import imaplib
import time
import email
# будильник
import threading

#То, что нужно будет передавать функциям

#Инициализация будильника
userName='Denis'
year_Alarm_Clock=2020
month_Alarm_Clock=3
day_Alarm_Clock=19
hour_Alarm_Clock=12
min_Alarm_Clock=49
sec_Alarm_Clock=0
#Инициализация парсера почты
gmail_user=''#Login
gmail_pass=''#Password

#Сами функции

#Будильник
def alarm_clock(year_Alarm_Clock, month_Alarm_Clock, day_Alarm_Clock, hour_Alarm_Clock, min_Alarm_Clock, sec_Alarm_Clock):
    dt = datetime.datetime(year_Alarm_Clock, month_Alarm_Clock, day_Alarm_Clock, hour_Alarm_Clock, min_Alarm_Clock, sec_Alarm_Clock)
    diff = (dt - datetime.datetime.now()).total_seconds()
    try:
        time.sleep(diff)
        print('сообщение в телегу текст')
    except:
        print('Нельзя поставить будильник в прошлое')
    return


# проверка почты на новое письмо gmail
# Нужно включить https://myaccount.google.com/lesssecureapps и https://mail.google.com/mail/u/2/#settings/fwdandpop

def check_email(gmail_user, gmail_pass):
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(gmail_user, gmail_pass)
    mail.list()
    count_Email_Start = (mail.select("inbox")[1][0]).decode('utf-8')
    while True:
        mail.list()
        count_Email_Current = (mail.select("inbox")[1][0]).decode('utf-8')
        if count_Email_Current > count_Email_Start:
            result, data = mail.search(None, "ALL")
            ids = data[0] # Получаем сроку номеров писем
            id_list = ids.split() # Разделяем ID писем
            latest_email_id = id_list[-1] # Берем последний ID
            result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем тело письма (RFC822) для данного ID
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            email_message_From = email_message['From']
            email_message_From = email_message_From[email_message_From.index('<'):email_message_From.index('>')]
            email_message_From = email_message_From[1:] 
            print('Отправить сообщение в телегу о том, что занят')
            print('Отправить "от кого" ', email_message_From)
            count_Email_Start = count_Email_Current
        time.sleep(15)  # частота проверки нового письма



#Чтобы запустить будильник 1, Парсер 2
Mode=2

#Для создания потока будильника передаются:
# Id юзера который поставил будильник, и значения времени которые он поставил. Поток создаётся с именем(id) юзера
if __name__ == '__main__':
    if Mode==1:
        Clock_Thread = threading.Thread(
            target = alarm_clock, name = userName, args=(year_Alarm_Clock,
                                                         month_Alarm_Clock,
                                                         day_Alarm_Clock,
                                                         hour_Alarm_Clock,
                                                         min_Alarm_Clock,
                                                         sec_Alarm_Clock))
        Clock_Thread.start()
    if Mode==2:
        check_email(gmail_user, gmail_pass)


# сценарии должны хранить логины и пароль
# запилить бота, возврат темы и отправителя в словаре.
