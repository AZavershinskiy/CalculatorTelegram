import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from bot_commands import *

load_dotenv()
secret_token = os.getenv('TOKEN')

app = ApplicationBuilder().token(secret_token).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('Server started')

app.run_polling()
