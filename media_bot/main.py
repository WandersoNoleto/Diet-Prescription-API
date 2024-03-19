from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, CallbackContext
from handlers import welcome_message
from telegram import Update
from youtube.hendlers_youtube import choose_download_option, handle_download_option, handle_link
from file_converter.handler_file import choose_file_type, handle_file_received, handle_conversion_option
import os

BOT_KEY = os.environ.get('BOT_KEY')

app = ApplicationBuilder().token(BOT_KEY).build()

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text and text.startswith('/'):
        await app.dispatcher.process_update(update, context)
    elif context.user_data.get('file_converter'):
        await handle_file_received(update, context)
    elif context.user_data.get('download_option'):
        await handle_link(update, context)

app.add_handler(CommandHandler("start", welcome_message))
app.add_handler(CallbackQueryHandler(choose_download_option, pattern='choose_download_option'))
app.add_handler(CallbackQueryHandler(handle_download_option, pattern='download_(video|audio)'))
app.add_handler(CallbackQueryHandler(choose_file_type, pattern='file_converter')) 
app.add_handler(CallbackQueryHandler(handle_conversion_option, pattern='convert_.*'))
app.add_handler(MessageHandler(None, handle_message)) 
app.run_polling()


