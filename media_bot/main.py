from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler
from handlers import welcome_message
from youtube.hendlers_youtube import choose_download_option, handle_download_option, handle_link
from file_converter.handler_file import choose_file_type
import os

BOT_KEY = os.environ.get('BOT_KEY')

app = ApplicationBuilder().token(BOT_KEY).build()

app.add_handler(CommandHandler("start", welcome_message))
app.add_handler(CallbackQueryHandler(choose_download_option, pattern='choose_download_option'))
app.add_handler(CallbackQueryHandler(handle_download_option, pattern='download_(video|audio)'))
app.add_handler(CallbackQueryHandler(choose_file_type, pattern='file_converter')) 
app.add_handler(MessageHandler(None, handle_link))

app.run_polling()
