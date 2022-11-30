from telegram import Update
from telegram.ext import ContextTypes

from spy import *


async def start(update: Update, context: ContextTypes):
    log(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f'Здравствуйте, {update.effective_user.first_name}!\nЯ БОТ - Калькулятор')


async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text('Команды:'
                                    '\n/sum - складывает два числа через пробел'
                                    '\n/help - отображает доступные команды'
                                    )


async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Введите два числа через пробел')
    msg = update.message.text
    items = msg.split()
    x = int(items[0])
    y = int(items[1])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{x} + {y} = {x+y}')


# async def echo(update: Update, context: ContextTypes):
#     log(update, context)
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
