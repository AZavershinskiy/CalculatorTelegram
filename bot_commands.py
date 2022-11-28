import datetime

from telegram import Update
from telegram.ext import ContextTypes

from spy import *


async def hi_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/sum\n/help')


async def time_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
