from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def welcome_message(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Download YouTube", callback_data='choose_download_option')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='''Hi, I am MediaBot! \n 
A Telegram bot for seamlessly managing media files. Whether you need to convert images, download videos from YouTube, or perform other media-related tasks, MediaBot has got you covered\n Choose one of the options below:''', 
                                   reply_markup=reply_markup)
