# -*- coding: utf-8 -*-

import telebot
from temp import google_t
import pdfkit
import time
import os
g =[]
bot = telebot.TeleBot('1394252827:AAGuyD-rDbQKc-2V9X1PtOCg4tEo8jaOtgs')
@bot.message_handler(content_types='text')
def start_message(message):
    p = open('users.txt', 'r+')
    for line in p:
        if line == message.cat.id:
            p.close()
            p=open('users.txt', 'a+').write("\n"+message.cat.id)
            p.close
        else:
            print('excec')
    for url in google_t(message.text):
        if message.text.find('https:\\') != 0:
                os.system('cls')
                pdfkit.from_url(url, 'pdf.pdf')
                f=open('pdf.pdf', 'rb')
                bot.send_document(message.chat.id, f)
                print('sleep_now')
                time.sleep(5)
                print('wake_up')
                f.close()
        else:
            bot.send_message(message.chat.id, 'Это ссылка')
    print(message.chat.username)
    bot.send_message(message.chat.id, 'Thats all')
bot.polling()