import telebot

botToken = '963013590:AAHHeETFLovUo7eCm32jtio3w1XQ9qcrGjU'
bot = telebot.TeleBot(botToken)


# telebot.apihelper.proxy = {'Socks4': '89.239.96.118:36521'}  #  -  прокси, если нужен в формате {'https':
# 'login:password@address:port'}


@bot.message_handler(commands=['start'])  # Реакция на команду start
def start_message(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать в Jarvis!\nЭто помощник, сценарии поведения которого настраиваются через '
                     'web-приложение на Flask\n')


def send_message(user_id, text):
    bot.send_message(user_id, text=text)
