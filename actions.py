#будильник
import time, datetime,imaplib,re, time
def Alarm_Clock():      
    dt=datetime.datetime(2020, 3, 18, 18, 6,15 )#дата срабатывания будильника (год,месяц,день,час,минута,секунда)
    diff = (dt - datetime.datetime.now()).total_seconds()
    print(diff)
    time.sleep(diff)
    print('сообщение в телегу текст')
    
#проверка почты на новое письмо gmail
#Нужно включить https://myaccount.google.com/lesssecureapps и https://mail.google.com/mail/u/2/#settings/fwdandpop
#
def Check_Email(gmail_user,gmail_pass):
    mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
    mail.login(gmail_user,gmail_pass)
    mail.list()
    count_Email_Start=(mail.select("inbox")[1][0]).decode('utf-8')
    while True:
        mail.list()
        count_Email_Current=(mail.select("inbox")[1][0]).decode('utf-8')
        if count_Email_Current > count_Email_Start:
            print('Отправить сообщение в телегу о том, а) занят б)текст')
            count_Email_Start=count_Email_Current
        time.sleep(15)#частота проверки нового письма
if __name__ == '__main__':
    Alarm_Clock()

#сценарии должны хранить логины и пароль 
#запилить бота, возврат темы и отправителя в словаре.
