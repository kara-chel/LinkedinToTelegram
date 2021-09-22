#!/usr/bin/env python3

from linkedin_mercuryo_io import linkedin_mercuryo_io
from telegram_mercuryo_io import telegram_mercuryo_io
import sqlite3
import logging

FORMAT = '%(asctime)s - [%(levelname)s] - %(name)s: %(message)s'


class Bot():
    conn = None
    cur = None

    def __init__(self):
        self.conn = sqlite3.connect('mercuryo_io.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS posts( id INT PRIMARY KEY, url TEXT, title TEXT );")

    def insert_post(self, post):
        self.cur.execute(f"INSERT INTO posts(id, url, title) VALUES(?, ?, ?);", (post['id'], post['url'], post['title']))
        self.conn.commit()

    def get_post(self, id):
        self.cur.execute(f"select * from posts where id='{id}'")
        return self.cur.fetchone()

    def process(self):
        lm = linkedin_mercuryo_io()
        posts = lm.get_posts()
        posts = lm.parse_posts(posts)
        items = []
        for post in posts[9::-1]:
            if not self.get_post(post['id']):
                logging.info('SEND TELEGRAM POST')
                self.insert_post(post)
                items.append(post)
        telegram_mercuryo_io(items)

    
if __name__ == '__main__':
    logging.basicConfig(format=FORMAT, filename="LinkedinToTelegram.log", level=logging.INFO)
    
    logging.info('Start bot')
    bot = Bot()
    bot.process()
    logging.info('Finish bot')

