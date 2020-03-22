import telebot

botToken = '1003282848:AAHM72fKodCByupZihiOdtTF1996fDsYB8A'
bot = telebot.TeleBot(botToken)


telebot.apihelper.proxy = {'Socks5': '247398282:247398282@orbtl.s5.opennetwork.cc:999'}  #  -  прокси, если нужен в формате {'https':
# 'login:password@address:port'}


@bot.message_handler(commands=['start'])  # Реакция на команду start
def start_message(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать в Jarvis!\nЭто помощник, сценарии поведения которого настраиваются через '
                     'web-приложение на Flask\n')


def send_message(user_id, text):
    bot.send_message(user_id, text=text)
