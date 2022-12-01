from telegram import Update
from telegram.ext import ContextTypes

from logs import *


async def start(update: Update, context: ContextTypes):
    log(update)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f'Здравствуйте, {update.effective_user.first_name}!\nЯ БОТ - Калькулятор')


async def help_command(update: Update):
    log(update)
    await update.message.reply_text('Команды:'
                                    '\n/sum - складывает два числа через пробел'
                                    '\n/help - отображает доступные команды'
                                    )


async def calc_command(update: Update, context: ContextTypes):
    log(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Введите два числа через пробел:')


async def math(update: Update, context: ContextTypes):
    msg = update.message.text
    item = msg.split()
    x = int(item[0])
    y = int(item[1])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=x+y)


# async def echo(update: Update, context: ContextTypes):
#     log(update)
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
