from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from youtube.yt_downloader import YoutubeDownloader


async def choose_download_option(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Download Video", callback_data='download_video')],
        [InlineKeyboardButton("Download Audio", callback_data='download_audio')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose the download option:', reply_markup=reply_markup)

async def handle_download_option(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.user_data['download_option'] = query.data
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me the YouTube video link.')

async def handle_link(update: Update, context: CallbackContext) -> None:
    link = update.message.text
    if context.user_data.get('download_option') == 'download_video' or context.user_data.get('download_option') == 'download_audio':
        downloader = YoutubeDownloader()
        if context.user_data['download_option'] == 'download_video':
            file_path = downloader.download_video(link)
            if file_path.startswith("An error occurred"):
                await context.bot.send_message(chat_id=update.effective_chat.id, text=file_path)
            else:
                await context.bot.send_video(chat_id=update.effective_chat.id, video=open(file_path, 'rb'))
        elif context.user_data['download_option'] == 'download_audio':
            file_path = downloader.download_audio(link)
            if file_path.startswith("An error occurred"):
                await context.bot.send_message(chat_id=update.effective_chat.id, text=file_path)
            else:
                await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(file_path, 'rb'))
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose the download option first.')

