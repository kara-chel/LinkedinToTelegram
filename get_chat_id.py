#!/usr/bin/env python3
import config
import telebot


def get_chat_id():
    bot = telebot.TeleBot(config.TELEGRAM_TOKEN, parse_mode='Markdown')

    @bot.message_handler(commands=['get_chat_id'])
    def welcome(message):
        bot.send_message(message.from_user.id, f'Ваш ChatID: {message.chat.id}')

    bot.polling(none_stop=False, interval=10)


if __name__ == '__main__':
    get_chat_id()