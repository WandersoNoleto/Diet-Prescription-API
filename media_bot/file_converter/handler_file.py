from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def choose_file_type(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🎥 Video", callback_data='convert_video')],
        [InlineKeyboardButton("🖼️ Image", callback_data='convert_image')],
        [InlineKeyboardButton("📄 Text", callback_data='convert_text')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='Choose the type of file you want to convert:', 
                                   reply_markup=reply_markup)
