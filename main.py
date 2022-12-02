import os

from dotenv import load_dotenv
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from bot_commands import *

load_dotenv()
secret_token = os.getenv('TOKEN')
app = ApplicationBuilder().token(secret_token).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), math))
print('Server started')

app.run_polling()
