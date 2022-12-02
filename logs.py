import datetime

from telegram import Update


def log(update: Update):
    file = open('logs.csv', 'a', encoding='utf-8')
    file.write(
        f'{now_log} - {update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()


now = datetime.datetime.now()
now_log = now.strftime('%y-%m-%d %H:%M:%S')
