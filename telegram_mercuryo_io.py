import config
import telebot


def telegram_mercuryo_io(posts):
    if len(posts) > 0:
        bot = telebot.TeleBot(config.TELEGRAM_TOKEN, parse_mode='Markdown')

        for post in posts:
            bot.send_message(config.TELEGRAM_CHAT_ID, text=f'[{post["title"]}]({post["url"]})')
