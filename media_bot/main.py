from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler
import os
from youtube.youtube_downloader import YoutubeDownloader

BOT_KEY = os.environ.get('BOT_KEY')

async def welcome_message(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Download YouTube Video", callback_data='download_video')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='Hello! I am MediaBot \n Choose one of the options below:', 
                                   reply_markup=reply_markup)

async def handle_link(update: Update, context: CallbackContext) -> None:
    link = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Got it, you want to download a YouTube video. Please wait while I process the video.')
    downloader = YoutubeDownloader()
    file_path = downloader.download_video(link)
    if file_path.startswith("An error occurred"):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=file_path)
    else:
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open(file_path, 'rb'))


async def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'download_video':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me the YouTube video link.')

app = ApplicationBuilder().token(BOT_KEY).build()
app.add_handler(CommandHandler("start", welcome_message))
app.add_handler(MessageHandler(None, handle_link))
app.add_handler(CallbackQueryHandler(button_click))

app.run_polling()
