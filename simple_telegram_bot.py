# -*- coding: utf-8 -*-
import telebot
import configparser


# Telegram Bot Authorization Token
config = configparser.ConfigParser()
config.read('token.ini')
TOKEN = config.get('TOKEN','TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello'])
def start(message):
    sent = bot.send_message(message.chat.id, 'What is your name?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    msg = 'Hello, {name}.'.format(name=message.text)
    bot.send_message(message.chat.id, msg)

def main():
    bot.polling()

if __name__ == '__main__':
    main()