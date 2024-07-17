import telebot
import schedule
import time
from datetime import datetime, timedelta
from st import parser


TOKEN = ''
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет!')


@bot.message_handler(commands=['check'])
def check(message):
    res = parser()
    bot.send_message(message.chat.id, res)


def job():
    res = parser()
    bot.send_message(838233811, res)

def gmt3_schedule(hour, minute):
    def job_wrapper():
        job()
    schedule.every().day.at(f"{hour:02}:{minute:02}").do(job_wrapper)


while True:
    try:
        bot.polling(none_stop=True, timeout=90)
        schedule.run_pending()
    except Exception as e:
        print(e)
        time.sleep(5)
        continue