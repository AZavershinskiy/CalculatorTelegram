import logging
import os

from dotenv import load_dotenv
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from bot_commands import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

load_dotenv()
secret_token = os.getenv('TOKEN')
app = ApplicationBuilder().token(secret_token).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), math))

app.run_polling()
