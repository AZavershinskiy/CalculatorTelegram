from telegram import Update
from telegram.ext import ContextTypes
import numexpr as ne


async def start_command(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f'Здравствуйте, {update.effective_user.first_name}!\nЯ БОТ - Калькулятор'
                                   '\nВсе отправленные сообщения без команд будут считаться арифметическими примерами, которые МНЕ нужно решить!'
                                   '\nДля подсказок введите: /help')


async def help_command(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='\nX ** Y - возводит X в степень Y'
                                   '\nX ** (1/Y) - извлечение корня из X, где Y величина корня'
                                   '\nX // Y - деление без остатка'
                                   '\nX % Y - получение остатка от деления'
                                   '\n\nПримеры со скобкам тоже решаются!'
                                   '\n\n/help - подсказки'
                                   '\n\n/start - начальное сообщение с приветствием')


async def math_f(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ответ: {ne.evaluate(update.message.text)}')
