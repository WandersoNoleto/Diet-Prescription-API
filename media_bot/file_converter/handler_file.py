from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from file_converter.converters import VideoConverter, TextConverter, ImageConverter
import os

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

async def handle_conversion_option(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    
    if data.startswith('convert_video'):
        await handle_video_conversion(update, context)
    elif data.startswith('convert_image'):
        await handle_image_conversion(update, context)
    elif data.startswith('convert_text'):
        await handle_text_conversion(update, context)

async def handle_video_conversion(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me the video file.')
    context.user_data['file_converter'] = True

async def handle_image_conversion(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me the image file.')
    context.user_data['file_converter'] = True

async def handle_text_conversion(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me the text file.')
    context.user_data['file_converter'] = True

async def handle_file_received(update: Update, context: CallbackContext) -> None:    
    query = update.callback_query
    data = query.data
    
    if data.startswith('convert_video'):
        file = context.bot.get_file(update.message.video.file_id)
        file_name = os.path.join('downloads', update.message.document.file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose the conversion option:', reply_markup=reply_markup_for_conversion_options('video'))
        video_converter = VideoConverter(file_name)
        await convert_video(update, context, video_converter, data)
        
    elif data.startswith('convert_image'):
        file = context.bot.get_file(update.message.photo)
        file_name = os.path.join('downloads', update.message.document.file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose the conversion option:', reply_markup=reply_markup_for_conversion_options('image'))
        image_converter = ImageConverter(file_name)
        await convert_image(update, context, image_converter, data)
        
    elif data.startswith('convert_text'):
        file = context.bot.get_file(update.message.document.file_id)
        file_name = os.path.join('downloads', update.message.document.file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please choose the conversion option:', reply_markup=reply_markup_for_conversion_options('text'))        
        text_converter = TextConverter(file_name)
        await convert_text(update, context, text_converter, data)


def reply_markup_for_conversion_options(file_type: str) -> InlineKeyboardMarkup:
    keyboard = []
    if file_type == 'video':
        keyboard = [
            [InlineKeyboardButton("MP4", callback_data='convert_video_mp4')],
            [InlineKeyboardButton("MOV", callback_data='convert_video_mov')],
            [InlineKeyboardButton("MKV", callback_data='convert_video_mkv')]
        ]
    elif file_type == 'image':
        keyboard = [
            [InlineKeyboardButton("JPG", callback_data='convert_image_jpg')],
            [InlineKeyboardButton("PNG", callback_data='convert_image_png')],
            [InlineKeyboardButton("GIF", callback_data='convert_image_gif')]
        ]
    elif file_type == 'text':
        keyboard = [
            [InlineKeyboardButton("TXT", callback_data='convert_text_txt')],
            [InlineKeyboardButton("DOCX", callback_data='convert_text_docx')],
            [InlineKeyboardButton("PDF", callback_data='convert_text_pdf')]
        ]
        
        
    return InlineKeyboardMarkup(keyboard)



async def convert_video(update: Update, context: CallbackContext, video_converter: VideoConverter, data: str) -> None:
    if data == 'convert_video_mp4':
        await video_converter.convert_to_mp4()
    elif data == 'convert_video_mov':
        await video_converter.convert_to_mov()
    elif data == 'convert_video_mkv':
        await video_converter.convert_to_mkv()
        
async def convert_image(update: Update, context: CallbackContext, image_converter: ImageConverter, data: str) -> None:
    if data == 'convert_video_mp4':
        await image_converter.convert_to_jpg()
    elif data == 'convert_video_mov':
        await image_converter.convert_to_png()
        
async def convert_text(update: Update, context: CallbackContext, text_converter: TextConverter, data: str) -> None:
    if data == 'convert_video_mp4':
        await text_converter.convert_to_txt()
    elif data == 'convert_video_mov':
        await text_converter.convert_to_pdf()
    elif data == 'convert_video_mkv':
        await text_converter.convert_to_docx()